from enum import Enum

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


class Choices(Enum):
    """
        This class allows modularity and defines a single source of truth
        for choices constants.

        TO-DO: Add rest of choices to this class
    """
    ATTRIBUTE_SKILL = "skill"
    ATTRIBUTE_TARGET = "target"
    ATTRIBUTE_EMOTION = "emotion"

    diary_attribute_choices = (
        (ATTRIBUTE_SKILL, "skill"),
        (ATTRIBUTE_TARGET, "skill"),
        (ATTRIBUTE_EMOTION, "skill")
    )
