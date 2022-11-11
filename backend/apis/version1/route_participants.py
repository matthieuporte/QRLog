from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.schemas import ParticipantsCreate
from db.session import get_db
from db.repository.participants import create_new_participant

router = APIRouter()

@router.post("/")
def create_participant(participant: ParticipantsCreate, db: Session = Depends(get_db)):
    participant = create_new_participant(participant=participant,db=db)
    return participant