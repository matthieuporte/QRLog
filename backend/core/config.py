import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime



# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
load_dotenv()

class Settings:
    PROJECT_NAME:str = "QRLog"
    PROJECT_VERSION:str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) 
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"



settings = Settings()
print("- - - -")
print(datetime.now().strftime("%H:%M:%S"))
print(settings.POSTGRES_USER,"on",settings.POSTGRES_SERVER,settings.POSTGRES_PORT)
print('- - - -')