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


def delete_event_with_id(id: int,db: Session):
    existing_event = db.query(Events).filter(Events.id == id)
    if not existing_event.first():
        return 0
    existing_event.delete(synchronize_session=False)
    db.commit()
    return 1