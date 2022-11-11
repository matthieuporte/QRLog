from fastapi import APIRouter

from apis.version1 import route_general_pages
from apis.version1 import route_participants


api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_participants.router,prefix="/participants",tags=["participants"])