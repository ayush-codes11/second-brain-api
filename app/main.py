from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.note import Note
from app.routers import home, notes
from app.routers import auth



app = FastAPI()

app.include_router(home.router)
app.include_router(notes.router)
app.include_router(auth.router)