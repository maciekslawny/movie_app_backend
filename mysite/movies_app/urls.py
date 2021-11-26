
from django.urls import path, include
from .views import MovieList, MovieDetail, add_movies_to_db, getMovies, list_movies, movieCreate, updateMovie

from rest_framework import routers

app_name = 'movies_app'


route = routers.DefaultRouter()
route.register("", MovieDetail, basename="moviedetail")


urlpatterns = [
    path('api/', include(route.urls)),
    path('api/movie-create/', movieCreate, name="movie-create"),
    path('api/movies/update/<int:pk>', updateMovie, name="update-movie"),    
    path('api/movies', MovieList.as_view(), name='listcreate'),

    path('add-movies/', add_movies_to_db, name='add-movies'),

    #path('api/movies', getMovies, name="get-movies"),
    #path('api/movies/<int:pk>', MovieDetail.as_view(), name='detailcreate'),
    #path('api/movies', list_movies, name='list_movies'),
]