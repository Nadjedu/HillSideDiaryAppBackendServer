from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import SkillSerializer
from ..models import Skill


class SkillViewSet(viewsets.ModelViewSet):
    lookup_field = "skill_uuid"
    serializer_class = SkillSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            # non staff users should only see active skills
            return Skill.objects.filter(active=True)

        return Skill.objects.all()

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "delete"\
                or self.action == "partial_update":
            permissions = [IsAuthenticated, IsAdminUser]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]
