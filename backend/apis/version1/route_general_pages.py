from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.db.models import models
from backend.db.session import get_db

templates = Jinja2Templates(directory="backend/templates")
general_pages_router = APIRouter()


@general_pages_router.get("/qr/{uuid}")
async def qr_page(request: Request, uuid: str, db: Session = Depends(get_db)):
    participant = (
        db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    )
    if participant is None:
        return templates.TemplateResponse(
            "general_pages/deliveryError.html",
            {
                "request": request,
                "message": "Le lien entré est erroné, merci de contacter l'administration",
                "eventname": "ERREUR",
            },
        )
    else:
        event = (
            db.query(models.Events)
            .filter(models.Events.id == participant.eventJoined)
            .first()
        )
        return templates.TemplateResponse(
            "general_pages/loadQR.html",
            {
                "request": request,
                "uuid": participant.uuid,
                "username": participant.username,
                "eventname": event.name,
            },
        )


@general_pages_router.get("/delivery/{uuid}")
async def delivery_page(request: Request, uuid: str, db: Session = Depends(get_db)):
    participant = (
        db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    )
    if participant is None:
        return templates.TemplateResponse(
            "general_pages/deliveryError.html",
            {
                "request": request,
                "message": "Le lien entré est erroné, merci de contacter l'administration",
                "eventname": "ERREUR",
            },
        )
    else:
        event = (
            db.query(models.Events)
            .filter(models.Events.id == participant.eventJoined)
            .first()
        )
        if participant.claimedTicket:
            message = participant.username + " a déja utilisé sa réservation !"
            return templates.TemplateResponse(
                "general_pages/deliveryError.html",
                {"request": request, "message": message, "eventname": event.name},
            )
        return templates.TemplateResponse(
            "general_pages/delivery.html",
            {
                "request": request,
                "uuid": participant.uuid,
                "username": participant.username,
                "eventname": event.name,
            },
        )
