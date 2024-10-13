from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Session

from . import crud, schemas, models
from .database import SessionLocal, engine

models.Base.metadata.creatr_all(bind=engine)
    
app = FastAPI()
    
# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Fastapi path operations

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users