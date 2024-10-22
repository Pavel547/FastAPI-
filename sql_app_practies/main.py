from fastapi import Depends, HTTPException, FastAPI #Import for path
from sqlalchemy.orm import Session #Import for path

import crud, models, schemas #Import for path
from .database import SessionLocal, engine #Import for Dependency


models.Base.metadata.creatr_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()