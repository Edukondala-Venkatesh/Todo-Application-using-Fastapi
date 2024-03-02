from sqlalchemy import Column, String, Integer,ForeignKey, DateTime, Boolean, func
from todo.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta, timezone



class User(Base):
    __tablename__ = 'user'

    id    = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    email  = Column(String, unique = True)
    password  = Column(String)

    todos = relationship("Blog", back_populates="creator")

    

class Blog(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now())
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    creator = relationship("User", back_populates="todos")

