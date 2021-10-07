from django.db import models

skills_categories = (
    ("Mindfulness", "Mindfulness"),
    ("Interpersonal Effectiveness", "Interpersonal Effectiveness"),
    ("Emotion Regulation", "Emotion Regulation"),
    ("Distress Tolerance", "Distress Tolerance"),
    ("Validation", "Validation")
)

target_categories = (
    ("Thoughts/Urges", "Thoughts/Urges"),
    ("Emotions/Feelings", "Emotions/Feelings"),
    ("Actions/Behaviors", "Actions/Behaviors")
)


class AttributeChoices(models.TextChoices):
    """
        This class allows modularity and defines a single source of truth
        for choices constants.

        TO-DO: Add rest of choices to this class
    """
    ATTRIBUTE_SKILL = ("skill", "skill")
    ATTRIBUTE_TARGET = ("target", "target")
    ATTRIBUTE_EMOTION = ("emotion", "emotion")


