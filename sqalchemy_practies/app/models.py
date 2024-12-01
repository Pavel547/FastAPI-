from sqlalchemy import Column, Integer, String, Boolean, Date

from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    description = Column(String)
    deadline = Column(Date, index=True)
    completed = Column(Boolean, index=True)    
