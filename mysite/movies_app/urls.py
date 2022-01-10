from django.urls import include, path
from rest_framework import routers

from .views import ActorsViewSet, DirectorsViewSet, MoviesViewSet

app_name = "movies_app"

router = routers.DefaultRouter()
router.register(r"actors", ActorsViewSet, basename="actors")
router.register(r"directors", DirectorsViewSet, basename="directors")
router.register(r"", MoviesViewSet, basename="movies")

urlpatterns = [
    path("", include(router.urls)),
]
