from sqlalchemy.orm import Session

from backend.db.models.models import Participants
from backend.schemas.schemas import ParticipantCreate


def create_new_participant(participant: ParticipantCreate, db: Session):
    participant = Participants(
        username=participant.username,
        email=participant.email,
        eventJoined=participant.eventJoined,
    )
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant


def delete_participant_with_uuid(uuid: str, db: Session):
    existing_participant = db.query(Participants).filter(Participants.uuid == uuid)
    if not existing_participant.first():
        return 0
    existing_participant.delete(synchronize_session=False)
    db.commit()
    return 1

    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String,unique=True,nullable=False)
    # email = Column(String,nullable=False,unique=True)
    # eventJoined =  Column(Integer,ForeignKey("events.id"))
    # uuid = Column(UUID(as_uuid=True), default=uuid.uuid4,index=True)
    # claimedTicket = Column(Boolean(),default=False))
