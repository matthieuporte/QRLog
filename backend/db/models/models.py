import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from backend.db.base_class import Base


class Events(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)


class Participants(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    eventJoined = Column(Integer, ForeignKey("events.id"), nullable=False)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    claimedTicket = Column(Boolean(), default=False)
