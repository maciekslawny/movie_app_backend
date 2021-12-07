from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.CharField(max_length=250, null=True)
    poster_url = models.CharField(max_length=5000, null=True)
    description = models.TextField(null=True)
    api_id = models.IntegerField()
    crew = models.ManyToManyField('Person', blank=True)
    
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
    ('other', 'Other'),
]

    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICE,
        blank=True
    )
    kind = models.CharField(
        max_length=50,
        choices=KIND_CHOICE,
        blank=True
    )
    biography = models.TextField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True, null=True)
    profile_path = models.CharField( blank=True, null=True, max_length=500)
    api_id = models.IntegerField()

    def __str__(self):
        return self.name 
    


    