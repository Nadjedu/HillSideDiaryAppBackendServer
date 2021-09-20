from django.urls import path, include
from rest_framework import routers

from .views import SkillViewSet

router = routers.SimpleRouter()
router.register(r'skills', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]