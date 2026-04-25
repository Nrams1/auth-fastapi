
from fastapi import FastAPI
from .routers import users






app = FastAPI()

#model.Base.metadata.create_all(bind=engine)



app.include_router(users.router)

""""
app.include_router(token.router)
"""


