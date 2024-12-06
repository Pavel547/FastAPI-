from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import crud, schemas, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()        

@app.post("/tasks_create/", response_model=schemas.TaskBase)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task_in_db = crud.get_task_by_name(db, name=task.task)
    if task_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task already exists")
    return crud.create_task(db=db, tasks=task)

@app.get("/tasks/", response_model=list[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_tasks = crud.get_all_tasks(db=db, skip=skip, limit=limit)
    return db_tasks

@app.get("/tasks/id/{task_id}", response_model=schemas.Task)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db=db, id=task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@app.get("/tasks/name/{task_name}", response_model=schemas.Task)
def get_tasks_by_name(task_name: str, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_name(db=db, name=task_name)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@app.get("/tasks/status/{task_status}", response_model=schemas.Task)
def get_task_by_status(task_status: bool, db: Session = Depends(get_db)):
    db_task = crud.get_tasks_by_status(db=db, status=task_status)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tasks not found")
    return db_task

@app.patch("/tasks/update/{task_name}", response_model=schemas.TaskBase)
def update_task_status(task_name: str, new_status: schemas.TaskBase, db: Session = Depends(get_db)):
    return crud.update_task_status(db=db, name=task_name, update_date=new_status)

@app.delete("/tasks/delet/{task_name}")
def delet_task(task_name: str, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.task==task_name).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Task not found")
    crud.del_task(db=db, task_del=task)
    return "Task was deleted"