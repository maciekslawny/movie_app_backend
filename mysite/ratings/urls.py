from django.urls import include, path
from rest_framework import routers

from .views import RatingsViewSet

app_name = "ratings"

router = routers.DefaultRouter()
router.register(r"", RatingsViewSet, basename="rating")

urlpatterns = [
    path("", include(router.urls)),
]
