from enum import Enum


class AudienceType(Enum):
    WORKING = "working"
    STUDYING = "studying"
    ELDERLY = "elderly"
    GRATITUDE = "gratitude"


AUDIENCE_PROMPTS = {
    AudienceType.WORKING: "a working professional starting their day.",
    AudienceType.STUDYING: "a student to stay focused on their studies.",
    AudienceType.ELDERLY: "an elderly person to stay active, positive and healthy.",
    AudienceType.GRATITUDE: "someone to express gratitude and appreciation.",
}
