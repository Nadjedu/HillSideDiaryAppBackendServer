from rest_framework import serializers

from ..models import Skill, Target, Emotion, DiaryAttribute, DiaryEntry, SudScore
from ..utils import validate_attribute_key


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

    def create(self, validated_data):
        skill = super(SkillSerializer, self).create(validated_data)
        skill.creator_uuid = self.context["request"].user
        skill.active = True  # seems like rest_framework sets this to False by default
        skill.save()

        return skill


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"

    def create(self, validated_data):
        target = super(TargetSerializer, self).create(validated_data)
        target.active = True
        target.creator_uuid = self.context["request"].user

        if not self.context["request"].user.is_staff:
            target.patient_uuid = self.context["request"].user

        target.save()
        return target


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = "__all__"

    def create(self, validated_data):
        emotion = super(EmotionSerializer, self).create(validated_data)
        emotion.active = True
        emotion.creator_uuid = self.context["request"].user
        emotion.save()

        return emotion


class DiaryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryAttribute
        fields = "__all__"
        extra_kwargs = {
            "type": {"required": True},
            "related_attribute_uuid": {"required": True}
        }

    def create(self, validated_data):
        # gotcha: no need to check for None objects, etc. Extra kwargs above will force super class to do that
        validate_attribute_key(validated_data.get("type"), validated_data.get("related_attribute_uuid"))
        return super(DiaryAttributeSerializer, self).create(validated_data)


class DiaryEntrySerializer(serializers.ModelSerializer):
    attributes = DiaryAttributeSerializer(many=True, required=False)

    def get_attributes(self, obj):
        """
        gotcha: Super class will look for method get_attributes() and assign the value to <attributes>
        :return all attributes related to the diary entity instance.
        """
        # gotcha: <instance>.<model_name>_set.all() is a reverse relationship accessor
        return DiaryAttributeSerializer(obj.diaryattributes_set.all(), many=True)

    def create(self, validated_data):
        entity = super(DiaryEntrySerializer, self).create(validated_data)
        entity.patient_uuid = self.context["request"].user
        entity.save()
        return entity

    class Meta:
        model = DiaryEntry
        fields = "__all__"


class SudScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudScore
        fields = "score"

    def create(self, validated_data):
        sud_score = super(SudScoreSerializer, self).create(validated_data)
        sud_score.patient_uuid = self.context["request"].user
        sud_score.save()
        return sud_score
