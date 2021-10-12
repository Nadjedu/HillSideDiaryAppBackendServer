import uuid

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import User
from .constants import AttributeChoices, SkillChoices, TargetChoices


class Skill(models.Model):
    skill_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill_name = models.CharField(max_length=50, null=True)
    skill_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(choices=SkillChoices.choices, null=True, max_length=100)


class Target(models.Model):
    """
        is_for_all: will allow you to create a set of core targets that every user.
        And if you want to create targets for specific users just assign the patient_uuid
        to their uuid.
        If you want even more fine grained permissions and groupings, django has
        a default Group table.
        Eg: Group.objects.get_or_create(name=<target_name>)
        And then, you could assign users to that group.
        This is very fine grained and will require a little bit of work on the queryset
        returned to the user (user has permission to view a target or it's a core target
        or target.patient_uuid = <request_user>).
        Check: https://docs.djangoproject.com/en/3.2/topics/auth/default/#groups

    """
    target_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Creator")
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Patient")
    target_name = models.CharField(max_length=50, null=True)
    target_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    is_for_all = models.BooleanField(default=False)
    category = models.CharField(choices=TargetChoices.choices, null=True, max_length=100)


class Emotion(models.Model):
    """
        is_for_all: check targets comment
    """
    emotion_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="emotion_creator")
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="emotion_patient")
    emotion_name = models.CharField(max_length=50, null=True)
    emotion_description = models.CharField(max_length=1000, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    is_for_all = models.BooleanField(default=False)


class DiaryEntry(models.Model):
    entry_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(null=True)
    mood_score = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(6)], default=6)
    note = models.CharField(max_length=5000, null=True)

    @property
    def attributes(self):
        return self.diaryattribute_set.all()


class SudScore(models.Model):
    score_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    patient_uuid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    score = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(10)])


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
