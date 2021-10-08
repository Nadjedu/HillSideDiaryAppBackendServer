from django.urls import path, include
from rest_framework import routers

from .views import SkillViewSet, TargetViewSet, EmotionViewSet, DiaryEntryViewSet, SudScoreViewSet

router = routers.SimpleRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'targets', TargetViewSet, basename='target')
router.register(r'emotions', EmotionViewSet, basename='emotion')
router.register(r'entries', DiaryEntryViewSet, basename='entry')
router.register(r'sud-scores', SudScoreViewSet, basename='sud-score')

urlpatterns = [
    path('', include(router.urls)),
]
