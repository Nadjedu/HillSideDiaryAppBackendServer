from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import SkillSerializer, TargetSerializer, EmotionSerializer, DiaryEntrySerializer
from ..models import Skill, Target, Emotion, DiaryEntry
from .permissions import CanActionTarget, CanRetrieveEmotion, CanActionDiaryEntity


class SkillViewSet(viewsets.ModelViewSet):
    lookup_field = "skill_uuid"
    serializer_class = SkillSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            # non staff users should only see active skills
            return Skill.objects.filter(active=True)

        return Skill.objects.all()

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "delete" \
                or self.action == "partial_update":
            permissions = [IsAuthenticated, IsAdminUser]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class TargetViewSet(viewsets.ModelViewSet):
    lookup_field = "target_uuid"
    serializer_class = TargetSerializer
    permission_classes = [IsAuthenticated, CanActionTarget]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Target.objects.all()

        return Target.objects.filter(patient_uuid=self.request.user)


class EmotionViewSet(viewsets.ModelViewSet):
    lookup_field = "emotion_uuid"
    serializer_class = EmotionSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Emotion.objects.all()

        return Emotion.objects.filter(patient_uuid=self.request.user)

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "delete" or \
                self.action == "partial_update":
            permissions = [IsAuthenticated, IsAdminUser]
        else:
            permissions = [IsAuthenticated, CanRetrieveEmotion]

        return [permission() for permission in permissions]


class DiaryEntryViewSet(viewsets.ModelViewSet):
    lookup_field = "entity_uuid"
    serializer_class = DiaryEntrySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return DiaryEntry.objects.all()

        return DiaryEntry.objects.filter(patient_uuid=self.request.user)

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            permissions = [IsAuthenticated, IsAdminUser | CanActionDiaryEntity]
        else:
            permissions = [IsAuthenticated, CanActionDiaryEntity]

        return [permission() for permission in permissions]
