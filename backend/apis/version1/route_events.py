import csv

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from backend.db.models import models
from backend.db.repository.events import create_new_event, delete_event_with_id
from backend.db.session import get_db
from backend.schemas.schemas import EventCreate

events_router = APIRouter()


# /!\ affiche les Id
@events_router.get("/")
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Events).all()
    return {"events": events}


@events_router.post("/")
async def init_event(
    name: str, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    eventInstance = EventCreate(name=name)
    event = create_new_event(event=eventInstance, db=db)
    datas = [el.decode("utf-8") for el in file.file.readlines()]
    try:
        # retirer csv_reader --> code a la main
        csv_reader = csv.DictReader(datas, delimiter=",")

        for row in csv_reader:
            participant = models.Participants(
                username=row["username"], email=row["email"], eventJoined=event.id
            )
            db.add(participant)

        db.commit()

    except Exception:
        return {"errorMessage": "There was an error uploading the file"}

    return {"message": f"L'evenement {name} a été créé avec succès"}


@events_router.delete("/{id}/delete")
def delete_event(id: int, db: Session = Depends(get_db)):
    message = delete_event_with_id(id=id, db=db)
    if not message:
        return {"errorMessage": "Aucun event trouvé avec cet id"}
    return {"msg": "Evenement supprimé."}
