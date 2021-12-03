from django.urls import path, include
from .views import MovieList, MovieDetail, ActorsList, DirectorsList, PersonDetail
from rest_framework import routers

app_name = 'movies_app'

route = routers.DefaultRouter()
route.register("", MovieDetail, basename="moviedetail")

urlpatterns = [
    path('actors/', ActorsList.as_view(), name='actors'),
    path('actors/<int:pk>', PersonDetail.as_view(), name='actordetail'),
    path('directors/', DirectorsList.as_view(), name='directors'),
    path('directors/<int:pk>', PersonDetail.as_view(), name='directordetail'),
    path('', MovieList.as_view(), name='movies'),
    path('<int:pk>', MovieDetail.as_view(), name='moviedetail'),
]