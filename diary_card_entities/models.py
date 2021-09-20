import uuid

from django.db import models
from django.utils import timezone

from accounts.models import User
from .constants import skills_categories


class Skill(models.Model):
    skill_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill_name = models.CharField(max_length=50, null=True)
    skill_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(choices=skills_categories, null=True, max_length=100)