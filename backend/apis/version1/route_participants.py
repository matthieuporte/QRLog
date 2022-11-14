from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.models import models
from backend.db.repository.participants import (
    create_new_participant,
    delete_participant_with_uuid,
)
from backend.db.session import get_db
from backend.schemas.schemas import ParticipantCreate

participants_router = APIRouter()


# /!\ affiche les Id
@participants_router.get("/")
def get_participants(db: Session = Depends(get_db)):
    participants = db.query(models.Participants).all()
    return {"participants": participants}


@participants_router.get("/{uuid}")
def get_participant(uuid: str, db: Session = Depends(get_db)):
    participant = (
        db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    )
    if participant is None:
        return {"errorMsg": "Aucun participant trouvé avec cet uuid"}
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #                     detail="Aucun participant trouvé avec cet uuid")
    return {
        "username": participant.username,
        #"email": participant.email,
        "eventJoined": participant.eventJoined,
        "claimedTicket": participant.claimedTicket,
    }


@participants_router.patch("/{uuid}/claim")
def patch_participant(uuid: str, db: Session = Depends(get_db)):
    participant = (
        db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    )
    if participant is None:
        return {"errorMsg": "Aucun participant trouvé avec cet uuid"}
    elif participant.claimedTicket:
        return {"errorMsg": "La réservation a deja été utilisée"}
    participant.claimedTicket = True
    event = (
        db.query(models.Events)
        .filter(models.Events.id == participant.eventJoined)
        .first()
    )
    db.commit()
    return templates.TemplateResponse(
        "general_pages/deliverySuccess.html",
        {"request": request, "message": "Retrait enregistré", "eventname": event.name},
    )


@participants_router.patch("/{uuid}/claim-undo")
def patch_participant_undo(uuid: str, db: Session = Depends(get_db)):
    participant = (
        db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    )
    if participant is None:
        return {"errorMsg": "Aucun participant trouvé avec cet uuid"}
    elif participant.claimedTicket:
        return {"errorMsg": "La réservation n'a pas encore été utilisée"}
    participant.claimedTicket = False
    db.commit()
    return participant


@participants_router.delete("/{uuid}/delete")
def delete_participant(uuid: str, db: Session = Depends(get_db)):
    code = delete_participant_with_uuid(uuid=uuid, db=db)
    if code == 0:
        return {"errorMsg": "Aucun participant trouvé avec cet uuid"}
    return {"msg": "Participant supprimé."}


@participants_router.post("/")
def post_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    participant = create_new_participant(participant=participant, db=db)
    return participant
