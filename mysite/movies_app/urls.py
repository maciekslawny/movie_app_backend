
from django.urls import path, include
from .views import MovieList, MovieDetail

from rest_framework import routers

app_name = 'movies_app'


route = routers.DefaultRouter()
route.register("", MovieDetail, basename="moviedetail")


urlpatterns = [

    path('', MovieList.as_view(), name='listcreate'),
    path('<int:pk>', MovieDetail.as_view(), name='detailcreate'),

    # path('add-movies/', add_movies_to_db, name='add-movies'),


]