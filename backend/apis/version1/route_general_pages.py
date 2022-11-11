from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

@general_pages_router.get("/qr")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/loadQR.html",{"request":request})


@general_pages_router.get("/err")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/deliveryError.html",{"request":request})




@general_pages_router.get("/delivery")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/delivery.html",{"request":request})