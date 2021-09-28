from django.shortcuts import get_object_or_404

from .constants import AttributeChoices
from .models import Skill, Target, Emotion


def validate_attribute_key(attribute_type, related_attribute_uuid):
    """
        Validator of attribute uuids. Pretty much enforcing a "foreign-key" relationship.
        Check Attribute table for more details or potential problems.

        Will raise validation error if none of these conditions are satisfied.
    """

    if attribute_type == AttributeChoices.ATTRIBUTE_SKILL:
        get_object_or_404(Skill, skill_uuid=related_attribute_uuid)
    elif attribute_type == AttributeChoices.ATTRIBUTE_TARGET:
        get_object_or_404(Target, target_uuid=related_attribute_uuid)
    else:
        get_object_or_404(Emotion, emotion_uuid=related_attribute_uuid)

    return

