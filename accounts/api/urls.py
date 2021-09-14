from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers

from .views import UserViewSet

# auto generates paths and urls
router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')

# url patterns for accounts package.
urlpatterns = [
    path('accounts/', include(router.urls)),
    path('accounts/token', TokenObtainPairView.as_view()),
    path('accounts/token/refresh', TokenRefreshView.as_view()),
]
