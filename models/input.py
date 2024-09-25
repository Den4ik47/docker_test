from pydantic import BaseModel


class Input(BaseModel):
    text: str
    sessionId: str