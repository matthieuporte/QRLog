from pydantic import BaseModel, EmailStr

class EventCreate(BaseModel):
    name: str

class ParticipantsCreate(BaseModel):
    username: str
    email: EmailStr