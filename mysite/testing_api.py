import requests

response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US&page=1')
cast_list = response.json()


for movie in cast_list['results']:
    print(movie)




'''
Lista filmow = ?

lista popularnych = https://api.themoviedb.org/3/movie/popular?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US&page=1

sciazka Poster filmu = https://image.tmdb.org/t/p/w500/1gxZrx9gL9ov2c1NpXimEUzMTmh.jpg


lista aktorw = ?


DANE O FILMIE - https://api.themoviedb.org/3/movie/3?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US

LISTA actors i directors dla danego filmu - https://api.themoviedb.org/3/movie/3/credits?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US

INFO o actor/director - https://api.themoviedb.org/3/person/16767?api_key=ad616d70a03f15fd5c01caf1b27911b0>>&language=en-US
'''