from sqlalchemy.orm import Session

from . import models, schemas

def create_task(db: Session, tasks: schemas.TaskCreate):
    db_task = models.Task(
        task=tasks.task,
        description=tasks.description,
        deadline=tasks.deadline,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id==task_id).filter()

def get_tasks_by_status(db: Session, status: bool):
    return db.query(models.Task).filter(models.Task.completed==status).all()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()
