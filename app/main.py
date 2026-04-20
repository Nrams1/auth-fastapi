from fastapi import FastAPI
from app.routers import sessions
from .routers import users


app = FastAPI()

app.include_router(users.router)
app.include_router(sessions.router)

