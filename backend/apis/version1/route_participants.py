from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from schemas.schemas import ParticipantCreate, ParticipantsRead
from db.models import models
from db.session import get_db
from db.repository.participants import create_new_participant, delete_participant_with_uuid

participants_router = APIRouter()


# /!\ affiche les Id 
@participants_router.get("/")
def get_participants(db: Session = Depends(get_db)):
    participants = db.query(models.Participants).all()
    return {"participants":participants}

@participants_router.get("/{uuid}")
def get_participant(uuid: str, db: Session = Depends(get_db)):
    participant = db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Aucun participant trouvé avec cet uuid")
    return {"username":participant.username,
            "email":participant.email,
            "eventJoined":participant.eventJoined,
            "claimedTicket":participant.claimedTicket}

@participants_router.patch("/{uuid}/claim")
def patch_participant(uuid: str, db: Session = Depends(get_db)):
    participant = db.query(models.Participants).filter(models.Participants.uuid == uuid, models.Participants.claimedTicket == False).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Aucun participant trouvé avec cet uuid")
    participant.claimedTicket = True
    db.commit()
    return participant

@participants_router.delete("/{uuid}/delete")
def delete_participant(uuid: str, db: Session = Depends(get_db)):
    message = delete_participant_with_uuid(uuid=uuid,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Aucun participant trouvé avec cet uuid : {uuid}")
    return {"msg":"Participant supprimé."}


@participants_router.post("/")
def post_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    participant = create_new_participant(participant=participant,db=db)
    return participant