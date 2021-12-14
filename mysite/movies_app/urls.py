from django.urls import include, path
from rest_framework import routers

from .views import Actors, Directors, Movies

app_name = "movies_app"

router = routers.DefaultRouter()
router.register(r"actors", Actors, basename="MyModel")
router.register(r"directors", Directors)
router.register(r"", Movies)

urlpatterns = [
    path("", include(router.urls)),
]
