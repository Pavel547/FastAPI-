from sqlalchemy.orm import Session

from . import schemas, models

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

def get_task_by_name(db: Session, task_name: str):
    return db.query(models.Task).filter(models.Task.task==task_name).first()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id==task_id).first()
    
def get_tasks_by_status(db: Session, task_status: bool):
    return db.query(models.Task).filter(models.Task.completed==task_status).all()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def update_task_status(db: Session, task_name: str, update_date: schemas.TaskBase):
    task = db.query(models.Task).filter(models.Task.task==task_name).first()
    task.completed = update_date.completed
    db.commit()
    db.refresh(task)
    return task

def del_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()