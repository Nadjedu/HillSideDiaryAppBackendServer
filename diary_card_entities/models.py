import uuid

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import User
from .constants import skills_categories, target_categories, AttributeChoices


class Skill(models.Model):
    skill_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill_name = models.CharField(max_length=50, null=True)
    skill_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(choices=skills_categories, null=True, max_length=100)


class Target(models.Model):
    target_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Creator")
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Patient")
    target_name = models.CharField(max_length=50, null=True)
    target_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(choices=target_categories, null=True, max_length=100)


class Emotion(models.Model):
    emotion_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="emotion_creator")
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="emotion_patient")
    emotion_name = models.CharField(max_length=50, null=True)
    emotion_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)


class DiaryEntry(models.Model):
    entry_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    sud_score = models.SmallIntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    note = models.CharField(max_length=5000, null=True)


class DiaryAttribute(models.Model):
    """
    Intermediate table for emotion, target and skill.

    Issue here: If the related attribute gets deleted then this table will point to a
    non-existing object.

    Potential fix: Django has a generic foreign key field (GenericForeignKey) but
    the database will outlive the application code and the whole setup is convoluted
    without a reference to the application code and/or Django docs.

    Check here for takes:
    https://lukeplant.me.uk/blog/posts/avoid-django-genericforeignkey/
    https://stackoverflow.com/questions/14333460/django-generic-foreign-keys-good-or-bad-considering-the-sql-performance
    """
    attribute_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    related_attribute_uuid = models.UUIDField(null=True, help_text="related entity uuid")
    diary_entity = models.ForeignKey(DiaryEntry, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=40, choices=AttributeChoices.choices)
    rating = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_created = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
