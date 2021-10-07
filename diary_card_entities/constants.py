from django.db import models

"""
    I guess we could say these are Django's version of enums.
"""


class AttributeChoices(models.TextChoices):
    ATTRIBUTE_SKILL = ("skill", "skill")
    ATTRIBUTE_TARGET = ("target", "target")
    ATTRIBUTE_EMOTION = ("emotion", "emotion")


class SkillChoices(models.TextChoices):
    SKILL_MINDFULNESS = ("Mindfulness", "Mindfulness")
    SKILL_INTERPERSONAL_EFFECTIVENESS = ("Interpersonal Effectiveness", "Interpersonal Effectiveness")
    SKILL_EMOTION_REGULATION = ("Emotion Regulation", "Emotion Regulation")
    SKILL_DISTRESS_TOLERANCE = ("Distress Tolerance", "Distress Tolerance")
    SKILL_VALIDATION = ("Validation", "Validation")


class TargetChoices(models.TextChoices):
    TARGET_THOUGHTS_URGES = ("Thoughts/Urges", "Thoughts/Urges")
    TARGET_EMOTIONS_FEELINGS = ("Emotions/Feelings", "Emotions/Feelings")
    TARGET_ACTIONS_BEHAVIOR = ("Actions/Behaviors", "Actions/Behaviors")
