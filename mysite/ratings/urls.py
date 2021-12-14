from django.urls import include, path
from rest_framework import routers

from .views import Ratings

app_name = "ratings"

router = routers.DefaultRouter()
router.register(r"", Ratings, basename="rating")

urlpatterns = [
    path("", include(router.urls)),
]
