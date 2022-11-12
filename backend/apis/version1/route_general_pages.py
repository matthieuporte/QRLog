from fastapi import APIRouter, HTTPException, Depends, status, Response, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from db.models import models
from db.session import get_db
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/qr/{uuid}")
async def home(request: Request,uuid: str, db: Session = Depends(get_db)):
    participant = db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    if (participant is None):
        return templates.TemplateResponse("general_pages/deliveryError.html",{
            "request":request,
            "message":"Le lien entré est erroné, merci de contacter l'administration",
            "eventname":"ERREUR"})
    else:
        event = db.query(models.Events).filter(models.Events.id == participant.eventJoined).first()
        return templates.TemplateResponse("general_pages/loadQR.html",{
            "request":request,
            "uuid":participant.uuid,
            "username":participant.username,
            "eventname":event.name})


@general_pages_router.get("/err/{name}")
async def home(request: Request,name:str):
    return templates.TemplateResponse("general_pages/deliveryError.html",{
        "request":request,
        "name": name})


@general_pages_router.get("/delivery/{uuid}")
async def home(request: Request,uuid:str, db: Session = Depends(get_db)):
    participant = db.query(models.Participants).filter(models.Participants.uuid == uuid).first()
    if (participant is None):
        return templates.TemplateResponse("general_pages/deliveryError.html",{
            "request":request,
            "message":"Le lien entré est erroné, merci de contacter l'administration",
            "eventname":"ERREUR"})
    else:
        event = db.query(models.Events).filter(models.Events.id == participant.eventJoined).first()
        if (participant.claimedTicket):
            message = participant.username + " a déja utilisé sa réservation !"
            return templates.TemplateResponse("general_pages/deliveryError.html",{
                "request":request,
                "message":message,
                "eventname":event.name})
        return templates.TemplateResponse("general_pages/delivery.html",{
            "request":request,
            "uuid":participant.uuid,
            "username":participant.username,
            "eventname":event.name})
