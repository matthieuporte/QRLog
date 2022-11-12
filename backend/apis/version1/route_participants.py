from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from schemas.schemas import ParticipantCreate, ParticipantsRead
from db.models import models
from db.session import get_db
from db.repository.participants import create_new_participant

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
    return {"username":participant.username,"email":participant.email}

@participants_router.patch("/{uuid}/claim")
def patch_participant(uuid: str, db: Session = Depends(get_db)):
    participant = db.query(models.Participants).filter(models.Participants.uuid == uuid, models.Participants.claimedTicket == False).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Aucun participant trouvé avec cet uuid")
    participant.claimedTicket = True
    db.commit()
    return participant


@participants_router.post("/")
def post_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    participant = create_new_participant(participant=participant,db=db)
    return participant