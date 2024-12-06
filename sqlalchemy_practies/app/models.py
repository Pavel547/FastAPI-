from sqlalchemy import Column, Integer, String, Date, Boolean

from .database import Base

class Task(Base):
    __tablename__="tasks"
    
    id = Column(Integer, index=True, primary_key=True)
    task = Column(String)
    description = Column(String)
    deadline = Column(Date, index=True)
    completed = Column(Boolean, index=True, default=False)
