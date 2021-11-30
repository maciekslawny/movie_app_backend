from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.CharField(max_length=250)
    poster_url = models.CharField(max_length=5000)
    description = models.TextField(max_length=50000)
    api_id = models.IntegerField()
    
    def __str__(self):
        return self.title

class Person(models.Model):

    GENDER_CHOICE = [
    ('male', 'Male'),
    ('famale', 'Famale'),
]

    KIND_CHOICE = [
    ('actor', 'Actor'),
    ('director', 'Director'),
]

    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICE,
    )
    kind = models.CharField(
        max_length=50,
        choices=KIND_CHOICE,
    )
    biography = models.TextField(max_length=5000)
    place_of_birth = models.CharField(max_length=200)
    api_id = models.IntegerField()

    def __str__(self):
        return self.name 
    


    