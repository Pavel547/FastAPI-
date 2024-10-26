from fastapi import Depends, HTTPException, FastAPI #Import for path
from sqlalchemy.orm import Session #Import for path

from . import schemas, crud, models #Import for path
from .database import SessionLocal, engine #Import for Dependency

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Function for create a owner

@app.post("/owners/", response_model=schemas.Owner) # Спробувати в response_model передати схему OwnerBase
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    owner = crud.get_owner_by_age(db, age=owner.age)
    if owner:
        raise HTTPException(status_code=400, detail="Owner already exists")
    return crud.create_owner(db=db, owner=owner)

# Function for returning the owner by id

@app.get("/owners/{owner_id}", response_model=schemas.Owner)
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    owner = crud.get_owner_by_id(db=db, id=owner_id)
    if owner is None:
        raise HTTPException(status_code=400, detail="Owner not found")
    return owner

# Function for returning owner by age

@app.get("/owners/{owners_age}", response_model=schemas.Owner)
def get_owner_by_age(owner_age: int, db: Session = Depends(get_db)):
    owner = crud.get_owner_by_age(db=db, age=owner_age)
    if owner is None:
        raise HTTPException(status_code=400, detail="Owners not found")
    return owner
    
# Function for feturing owners

@app.get("/owners/", response_model=list[schemas.Owner])
def get_owners(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    owners = crud.get_owners(db=db, skip=skip, limit=limit)
    return owners

# Function for create Vehicle

@app.post("/owners/{owners_id}/vehicles/", response_model=schemas.Vehicle)
def create_vehicle(owner_id: int, vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    vehicle = crud.create_owner_vehicle(db=db, vehicle=vehicle, user_id=owner_id)
    if vehicle: 
        raise HTTPException(status_code=400, detail="Vehicle for user alredy exists")
    return crud.create_owner_vehicle(db=db, vehicle=vehicle, owner_id=owner_id)

# Function for get vehicle by id

@app.get("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def get_vehicle_by_id(vehicle_id, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle_by_id(db=db, vehicle_id=vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=400, detail="Vehicle does not exist")
    return vehicle

# Function for get vehicle by year

@app.get("/vehicles/{year}", response_model=schemas.Vehicle)
def get_vehicle_by_year(year: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicles_by_year(db=db, year=year)
    if vehicle is None:
        raise HTTPException(status_code=400, detail="Vehicles this year does not exists")
    return vehicle
    
# Function for get vehicle by type

@app.get("/vehicles/{vehicles_type}", response_model=schemas.Vehicle)
def get_vehicle_by_type(vehicles_type: str, db: Session = Depends(get_db)):
    vehicles = crud.get_vehicles_by_type(db=db, type=vehicles_type)
    if vehicles is None:
        raise HTTPException(status_code=400, detail="Vehicles this year does not exists")
    return vehicles
    
# Function for get vehicle by brand

@app.get("/vehicles/{brand}", response_model=schemas.Vehicle)
def get_vehicle_by_brand(brand:str, db: Session = Depends(get_db)):
    vehicles = crud.get_vehicles_by_brand(db=db, brand=brand)
    if vehicles is None:
        raise HTTPException(status_code=400, detail="Vehicle this brand does not exists")
    return vehicles

# Function for get vehicles
@app.get("/vechicles/", response_model=list[schemas.Vehicle])
def get_vehicles(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    vehicles = crud.get_vehicles(db=db, skip=skip, limit=limit)
    return vehicles
    
# Function for re registr Owner

@app.patch("/owners/{owner_id}", response_model=schemas.OwnerBase)
def re_registr_owner(owner_id: int, newdata: schemas.OwnerBase, db: Session = Depends(get_db)):
    return crud.re_registration_owner(db=db, id=owner_id, update_data=newdata)
        
# Function for delet owner

@app.delete("/owners/{owner_id}")
def del_owner(owner_id: int, db: Session = Depends(get_db)):
    owner = db.query(models.Owner).filter(models.Owner.owner_id == owner_id)
    if owner is None:
        raise HTTPException(status_code=400, detail="Owner not found")
    crud.del_owner(db=db, owner=owner)
    return "Owner has been removed"