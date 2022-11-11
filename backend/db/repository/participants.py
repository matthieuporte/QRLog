from sqlalchemy.orm import Session

from schemas.schemas import ParticipantsCreate
from db.models.models import Participants
from sqlalchemy.dialects.postgresql import UUID
import uuid

def create_new_participant(participant:ParticipantsCreate,db:Session):
    participant = Participants(username=participant.username,
        email = participant.email,
        claimedTicket=False)
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant
                
                               
    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String,unique=True,nullable=False)
    # email = Column(String,nullable=False,unique=True)
    # eventJoined =  Column(Integer,ForeignKey("events.id"))
    # uuid = Column(UUID(as_uuid=True), default=uuid.uuid4,index=True)
    # claimedTicket = Column(Boolean(),default=False))