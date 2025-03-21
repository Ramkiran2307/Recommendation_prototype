from pydantic import BaseModel

class MoodInput(BaseModel):
    mood: str
