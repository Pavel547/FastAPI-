from pydantic import BaseModel

from datetime import date

class TaskBase(BaseModel):
    task: str
    description: str
    deadline: date
    
class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool | None = None
    