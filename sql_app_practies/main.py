from fastapi import Depends, HTTPException, FastAPI #Import for path
from sqlalchemy.orm import Session #Import for path

import crud, models, schemas #Import for path
from .database import SessionLocal, engine #Import for Dependency

app = FastAPI()

models.Base.metadata.creatr_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Function for create a owner

@app.post("/owners/", response_model=schemas.Owner)
def create_owner(owner:schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_by_age(db, age=owner.age)
    if db_owner:
        raise HTTPException(status_code=400, detail="Owner already exists")
    return crud.create_owner(db=db, owner=owner)

# Function for returning the owner by id

@app.get("/owners/{owner_id}", response_model=models.Owner)
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_by_id(db=db, id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owner not found")
    return db_owner

# Function for returning owner by age

@app.get("/owners/{owners_age}", response_model=schemas.Owner)
def get_owner_by_age(owner_age: int, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_by_age(db=db, age=owner_age)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owners not found")
    
# Function for feturing owners

@app.get("/owners/", response_model=list[schemas.Owner])
def get_owners(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    owners = crud.get_owners(db=db, skip=skip, limit=limit)
    return owners