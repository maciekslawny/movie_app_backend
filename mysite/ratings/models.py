from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from movies_app.models import Movie

# Create your models here.


class Rating(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "movie"]

    def __str__(self):
        return f"{self.movie.title} {self.user.email}"
