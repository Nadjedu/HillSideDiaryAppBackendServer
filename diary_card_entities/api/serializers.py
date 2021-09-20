from rest_framework import serializers

from ..models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

    def create(self, validated_data):
        skill = super(SkillSerializer, self).create(validated_data)
        skill.creator_uuid = self.context["request"].user
        skill.active = True # seems like rest_framework sets this to False by default
        skill.save()

        return skill
