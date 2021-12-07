from django.urls import path, include
from .views import Movies, Actors, Directors
from rest_framework import routers

app_name = 'movies_app'

router = routers.DefaultRouter()
router.register(r'actors', Actors)
router.register(r'directors', Directors)
router.register(r'', Movies)

urlpatterns = [
    path('', include(router.urls)),
]