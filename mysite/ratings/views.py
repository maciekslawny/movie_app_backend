# Create your views here.
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from movies_app.models import Movie
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Rating
from .serializers import RatingSerializer


class Ratings(viewsets.ModelViewSet):
    serializer_class = RatingSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        if self.request.method == "PUT":
            print(self.request.data["value"])
            created = Rating.objects.update_or_create(
                movie=Movie.objects.get(id=item),
                user=CustomUser.objects.get(id=self.request.user.id),
                defaults={"value": self.request.data["value"]},
            )

            item = get_object_or_404(Rating, movie=item, user=self.request.user.id)
            print("PUT")
            return item

        print(get_object_or_404(Rating, movie=item, user=self.request.user.id))
        return get_object_or_404(Rating, movie=item, user=self.request.user.id)

    def get_queryset(self):
        print(self.request.user.id)
        return Rating.objects.all()
