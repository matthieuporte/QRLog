from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/qr/{uuid}")
async def home(request: Request,uuid:str):
    return templates.TemplateResponse("general_pages/loadQR.html",{
        "request":request,
        "uuid":uuid})


@general_pages_router.get("/err/{name}")
async def home(request: Request,name:str):
    return templates.TemplateResponse("general_pages/deliveryError.html",{
        "request":request,
        "name": name})



@general_pages_router.get("/delivery")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/delivery.html",{"request":request})