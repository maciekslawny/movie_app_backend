from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.CharField(max_length=250)
    poster_url = models.CharField(max_length=5000)
    description = models.CharField(max_length=50000)
    api_id = models.IntegerField()
    
    class Meta:
        pass

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.IntegerField()
    biography = models.CharField(max_length=5000)
    place_of_birth = models.CharField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return self.name 
    

class Director(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.IntegerField()
    biography = models.CharField(max_length=5000)
    place_of_birth = models.CharField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return self.name 
    