from db.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Logstats(Base):
    __tablename__ = 'loginstats'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='username')
    last_seen = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
