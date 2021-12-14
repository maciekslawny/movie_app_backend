from django.urls import include, path
from rest_framework import routers

from .views import Users

app_name = "users"

router = routers.DefaultRouter()
router.register(r"", Users)

router = routers.DefaultRouter()
router.register(r'', Users)

urlpatterns = [
    path("", include(router.urls)),
]
