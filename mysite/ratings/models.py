from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Rating(models.Model):
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey("movies_app.Movie", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "movie"]

    def __str__(self):
        return f"{self.movie.title} {self.user.email}"
