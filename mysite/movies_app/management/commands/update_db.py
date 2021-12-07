from django.core.management.base import BaseCommand, CommandError
from movies_app.models import Person, Movie
import requests

class Command(BaseCommand):
    help = 'Retrieves Movies & Peoples from API'

    def handle(self, *args, **options):
        popular_movies = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US&page=1').json()

        def adding_persons(crew_api_ids): 
            
            for person_api_id in crew_api_ids:

                if Person.objects.filter(api_id=person_api_id):
                    print(person_api_id, 'Osoba już w bazie')
                    continue

                person_response = requests.get(f'https://api.themoviedb.org/3/person/{person_api_id}?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US').json()

                if person_response['known_for_department'] == "Acting":
                    kind = 'actor'
                elif person_response['known_for_department'] == "Directing":
                    kind = 'director'
                else:
                    kind = 'other'

                gender = ''
                if person_response['gender'] == 1:
                    gender = 'famale'
                elif person_response['gender'] == 2:
                    gender = 'male'

                if person_response['profile_path']:
                    profile_path = 'https://image.tmdb.org/t/p/w200/' + str(person_response['profile_path'])
                else:
                    profile_path = None


                Person.objects.create(
                    name=person_response['name'],
                    birthday = person_response['birthday'],
                    gender = gender,
                    kind = kind,
                    profile_path = profile_path,
                    biography = person_response['biography'],
                    place_of_birth = person_response['place_of_birth'],
                    api_id = person_api_id,
                )

      
        for movie in popular_movies['results']:

            if Movie.objects.filter(api_id=movie['id']):
                print(movie['title'], 'JUZ W BAZIe')
                continue
            
            print('Dodawanie..', movie['title'])
            movie_cast = requests.get(f'https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US').json()['cast']
            
            crew_api_ids = [person['id'] for person in movie_cast]
            adding_persons(crew_api_ids)

            added_movie = Movie.objects.create(
                title=movie['title'],
                release_date= 2000,
                poster_url= 'https://image.tmdb.org/t/p/w200/' + str(movie['poster_path']),
                description= movie['overview'][:400],
                api_id = movie['id'],     
            )

            for api_id in crew_api_ids:
                print('Api ID:', api_id)
                person = Person.objects.get(api_id=api_id)
                added_movie.crew.add(person)
        
    
