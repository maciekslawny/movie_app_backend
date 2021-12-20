# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from movies_app.models import Movie
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Rating
from .serializers import RatingSerializer


class RatingsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        if self.request.method == "PUT":
            print(self.request.data["value"])
            created = Rating.objects.update_or_create(
                movie=Movie.objects.get(id=item),
                user=get_user_model().objects.get(id=self.request.user.id),
                defaults={"value": self.request.data["value"]},
            )

            item = get_object_or_404(Rating, movie=item, user=self.request.user.id)
            print("PUT")
            return item

        print(get_object_or_404(Rating, movie=item, user=self.request.user.id))
        return get_object_or_404(Rating, movie=item, user=self.request.user.id)
