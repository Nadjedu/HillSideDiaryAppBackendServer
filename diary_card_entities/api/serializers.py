from rest_framework import serializers
from django.utils import timezone
from django.db import transaction

from ..models import Skill, Target, Emotion, DiaryAttribute, DiaryEntry, SudScore
from ..utils import validate_attribute_key


class EditableEntitySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        is_for_all = validated_data.pop("is_for_all", None)
        entity = super().create(validated_data)
        entity.active = True
        entity.creator_uuid = self.context["request"].user

        # staff logic for creating entity
        if self.context["request"].user.is_staff:
            if is_for_all:
                entity.is_for_all = is_for_all

        # patient logic for creating entity
        if not self.context["request"].user.is_staff:
            entity.patient_uuid = self.context["request"].user

        entity.save()
        return entity

    def update(self, instance, validated_data):
        is_for_all = validated_data.pop("is_for_all", None)
        entity = super().update(instance, validated_data)

        # only staff should be able to update is_for_all
        if is_for_all and self.context["request"].user.is_staff:
            entity.is_for_all = is_for_all
            entity.save()

        return entity


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        extra_kwargs = {
            "category": {"required": True}
        }

    def create(self, validated_data):
        skill = super(SkillSerializer, self).create(validated_data)
        skill.creator_uuid = self.context["request"].user
        skill.active = True  # seems like rest_framework sets this to False by default
        skill.save()

        return skill

    def update(self, instance, validated_data):
        skill = super().update(instance, validated_data)
        skill.date_modified = timezone.now
        return skill.save()


class TargetSerializer(EditableEntitySerializer):
    class Meta:
        model = Target
        fields = "__all__"
        extra_kwargs = {
            "category": {"required": True}
        }


class EmotionSerializer(EditableEntitySerializer):
    class Meta:
        model = Emotion
        fields = "__all__"


class DiaryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryAttribute
        fields = "__all__"
        extra_kwargs = {
            "type": {"required": True},
            "related_attribute_uuid": {"required": True}
        }

    def create(self, validated_data):
        # gotcha: no need to check for None objects, etc. Extra kwargs above will force class to do that
        validate_attribute_key(validated_data.get("type"), validated_data.get("related_attribute_uuid"))
        return super(DiaryAttributeSerializer, self).create(validated_data)


class DiaryEntrySerializer(serializers.ModelSerializer):
    attributes = DiaryAttributeSerializer(many=True, required=False)

    @transaction.atomic
    def create(self, validated_data):
        attributes_data = validated_data.pop("attributes", None)
        entity = super(DiaryEntrySerializer, self).create(validated_data)
        entity.patient_uuid = self.context["request"].user
        entity.save()

        # validate and create attributes
        for attribute_data in attributes_data:
            attribute = DiaryAttribute(diary_entity=entity)
            diary_serializer = DiaryAttributeSerializer(attribute, data=attribute_data)
            if diary_serializer.is_valid():
                diary_serializer.save()
            else:
                raise serializers.ValidationError(diary_serializer.errors)

        return entity

    class Meta:
        model = DiaryEntry
        fields = "__all__"


class SudScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudScore
        fields = "__all__"

    def create(self, validated_data):
        sud_score = super(SudScoreSerializer, self).create(validated_data)
        sud_score.patient_uuid = self.context["request"].user
        sud_score.save()
        return sud_score
