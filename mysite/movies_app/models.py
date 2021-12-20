from django.db import models
from django.db.models import Avg
from ratings.models import Rating


class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.CharField(max_length=5000, null=True)
    description = models.TextField(null=True)
    api_id = models.IntegerField()
    crew = models.ManyToManyField("Person", related_name="test", blank=True)

    @property
    def get_ratings_amount(self):
        ratings_list = Rating.objects.filter(movie=self.pk)
        return len(ratings_list)

    @property
    def get_ratings_average(self):
        average_value = Rating.objects.filter(movie=self.pk).aggregate(Avg("value"))
        return average_value["value__avg"]

    @property
    def get_cast_actors(self):
        return self.crew.filter(kind="actor")

    @property
    def get_cast_directors(self):
        return self.crew.filter(kind="director")

    def __str__(self):
        return self.title


class Person(models.Model):

    GENDER_CHOICE = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    KIND_CHOICE = [
        ("actor", "Actor"),
        ("director", "Director"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE, blank=True)
    kind = models.CharField(max_length=50, choices=KIND_CHOICE, blank=True)
    biography = models.TextField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True, null=True)
    profile_path = models.CharField(blank=True, null=True, max_length=500)
    api_id = models.IntegerField()

    def __str__(self):
        return self.name
