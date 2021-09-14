from rest_framework import serializers

from ..models import Skills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['record_number', 'client_id', 'skill_code', 'skill_description',
        'note','date_added','date_modified', 'active']