from django.contrib.auth.models import User
from django.test import TestCase

from .models import Movie

# Create your tests here.


class Test_Movie(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_movie = Movie.objects.create(
            title="Testowy Film",
            release_date=2000,
            poster_url="/przykladowy.jpg",
            description="przykladowy opis",
            api_id=123,
        )
        testuser1 = User.objects.create_user(
            username="test_user1", password="123456789"
        )

    def test_movie_content(self):
        movie = Movie.objects.get(api_id=123)
        title = f"{movie.title}"
        release_date = f"{movie.release_date}"
        poster_url = f"{movie.poster_url}"

        self.assertEqual(title, "Testowy Film")
        self.assertEqual(poster_url, "/przykladowy.jpg")
        self.assertEqual(str(movie), "Testowy Film")
