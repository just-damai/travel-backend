from enum import Enum
from pydantic import BaseModel

class Emotion(str, Enum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    SURPRISED = "surprised"

class TranslateRequest(BaseModel):
    text: str
    emotion: Emotion = Emotion.NEUTRAL

class TranslateResponse(BaseModel):
    original: str
    translation: str
    emotion: Emotion