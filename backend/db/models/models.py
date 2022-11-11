from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from db.base_class import Base

class Events(Base):
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String,nullable=False)

class Participants(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    eventJoined =  Column(Integer,ForeignKey("events.id"))
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4,index=True)
    claimedTicket = Column(Boolean(),default=False)
