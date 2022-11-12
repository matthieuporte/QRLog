from fastapi import APIRouter

from backend.apis.version1 import (route_events, route_general_pages,
                                   route_participants)

api_router = APIRouter()
api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["general_pages"]
)
api_router.include_router(
    route_participants.participants_router,
    prefix="/participants",
    tags=["participants"],
)
api_router.include_router(route_events.events_router, prefix="/events", tags=["events"])
