from pydantic import BaseModel

from datetime import date

class TaskBase(BaseModel):
    task: str
    description: str | None = None
    deadline: date
    completed: bool
    
class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
