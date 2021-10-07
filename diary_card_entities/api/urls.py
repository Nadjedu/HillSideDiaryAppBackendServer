from django.urls import path, include
from rest_framework import routers

from .views import SkillViewSet, TargetViewSet

router = routers.SimpleRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'targets', TargetViewSet, basename='target')

urlpatterns = [
    path('', include(router.urls)),
]