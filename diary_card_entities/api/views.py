from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import SkillSerializer, TargetSerializer, EmotionSerializer, DiaryEntrySerializer, SudScoreSerializer
from ..models import Skill, Target, Emotion, DiaryEntry, SudScore
from .permissions import CanActionTarget, CanRetrieveEmotion, CanActionDiaryEntity, CanActionSudScore


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
    permission_classes = [IsAuthenticated, CanActionTarget | IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Target.objects.all()

        return Target.objects.filter(patient_uuid=self.request.user) | Target.objects.filter(is_for_all=True)


class EmotionViewSet(viewsets.ModelViewSet):
    lookup_field = "emotion_uuid"
    serializer_class = EmotionSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Emotion.objects.all()

        return Emotion.objects.filter(patient_uuid=self.request.user) | Emotion.objects.filter(is_for_all=True)

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "delete" or \
                self.action == "partial_update":
            permissions = [IsAuthenticated, IsAdminUser]
        else:
            permissions = [IsAuthenticated, CanRetrieveEmotion | IsAdminUser]

        return [permission() for permission in permissions]


class DiaryEntryViewSet(viewsets.ModelViewSet):
    lookup_field = "entry_uuid"
    serializer_class = DiaryEntrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_added"]  # allows filtering by dd/mm/yyyy

    def get_queryset(self):
        month = self.request.query_params.get("month")
        year = self.request.query_params.get("year")
        qs = DiaryEntry.objects.all().prefetch_related("diaryattribute_set")

        # allows filtering by mm/yyyy
        if month and year:
            qs = qs.filter(date_added__month=month, date_added__year=year)

        if self.request.user.is_staff:
            return qs

        return qs.filter(patient_uuid=self.request.user)

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            permissions = [IsAuthenticated, IsAdminUser | CanActionDiaryEntity]
        else:
            permissions = [IsAuthenticated, CanActionDiaryEntity]

        return [permission() for permission in permissions]


class SudScoreViewSet(viewsets.ModelViewSet):
    lookup_field = "score_uuid"
    serializer_class = SudScoreSerializer
    queryset = SudScore.objects.all()
    permission_classes = [IsAuthenticated, CanActionSudScore | IsAdminUser]
