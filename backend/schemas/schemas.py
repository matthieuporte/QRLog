from pydantic import BaseModel, EmailStr
from typing import List

class EventCreate(BaseModel):
    name: str

class ParticipantsCreate(BaseModel):
    username: str
    email: EmailStr

class ParticipantRead(BaseModel):
    username:str
    email: EmailStr
    uuid: str
    claimedTicket:bool

class ParticipantsRead(BaseModel):
    participant: List[ParticipantRead]