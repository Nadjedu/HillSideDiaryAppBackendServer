from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers

from .views import UserViewSet

# auto generates paths and urls
router = routers.SimpleRouter()
router.register(r'skills', UserViewSet, basename='skills')

# url patterns for accounts package.
urlpatterns = [
]
