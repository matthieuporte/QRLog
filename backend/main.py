from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.base import api_router
from db.session import engine
from db.base import Base


def include_router(app):
	app.include_router(api_router)

def configure_static(app): 
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
	Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app 


app = start_application()


# route get list event
# route post crée event
# bouton vert qui patch (formulaire)
# route delivery reset
# csv to db (bulk post)
# event nullable = False
# link event to participant
# route get pour tout les participants qui ne montre pas l'id
# corriger les general_pages_routes