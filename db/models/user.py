from db.base import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    time_created = Column(DateTime(), server_default=func.now())
