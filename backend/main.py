from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.apis.base import api_router
from backend.core.config import settings


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="backend/static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)

    return app


app = start_application()


# emails: how to call api with fastapi
