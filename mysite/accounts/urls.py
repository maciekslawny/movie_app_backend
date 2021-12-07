from django.urls import path, include
from .views import Users
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'', Users)

urlpatterns = [
    path('', include(router.urls)),
]
