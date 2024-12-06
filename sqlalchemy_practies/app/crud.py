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

def get_task_by_name(db: Session, name: str):
    return db.query(models.Task).filter(models.Task.task==name).first()

def get_task_by_id(db: Session, id: int):
    return db.query(models.Task).filter(models.Task.id==id).first()
    
def get_tasks_by_status(db: Session, status: bool):
    return db.query(models.Task).filter(models.Task.completed==status).all()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def update_task_status(db: Session, name: str, update_date: schemas.TaskBase):
    task = db.query(models.Task).filter(models.Task.task==name).first()
    task.completed = update_date.completed
    db.commit()
    db.refresh(task)
    return task

def del_task(db: Session, task_del: models.Task):
    db.delete(task_del)
    db.commit()