from rest_framework import serializers

from ..models import Skill, Target


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
