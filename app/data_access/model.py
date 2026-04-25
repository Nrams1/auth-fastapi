
from sqlalchemy import Column, Engine, Integer, String
from app.data_access.db import Base
from app.data_access.db import engine





class User(Base):
     __tablename__ = 'users1'
     id = Column(Integer, primary_key=True)
     email = Column(String, unique=True)
     password = Column(String, unique=False ,nullable=False)

Base.metadata.create_all(bind=engine)
