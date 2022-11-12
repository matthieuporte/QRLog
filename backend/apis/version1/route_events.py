from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from schemas.schemas import EventCreate, EventsRead
from db.models import models
from db.session import get_db
from db.repository.events import create_new_event, delete_event_with_id

events_router = APIRouter()


# /!\ affiche les Id 
@events_router.get("/")
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Events).all()
    return {"events":events}

@events_router.post("/")
def post_event(event: EventCreate, db: Session = Depends(get_db)):
    event = create_new_event(event=event,db=db)
    return event

@events_router.delete("/{id}/delete")
def delete_event(id: int, db: Session = Depends(get_db)):
    message = delete_event_with_id(id=id,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Aucun evenvement trouvé avec cet id : {id}")
    return {"msg":"Evenement supprimé."}