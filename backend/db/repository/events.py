from sqlalchemy.orm import Session

from schemas.schemas import EventCreate, ParticipantRead
from db.models.models import Events

def create_new_event(event:EventCreate,db:Session):
    event = Events(
        name = event.name
        )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event