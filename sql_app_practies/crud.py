from sqlalchemy.orm import Session
from . import models, schemas

def get_owner_by_id(db: Session, id: int):
    return db.query(models.Owner).filter(models.Owner.owner_id == id).first()

def get_owner_by_age(db:Session, age: int):
    return db.query(models.Owner).filter(models.Owner.age == age).all()

def get_owners(db: Session, skip: int = 0, limit: int = 15):
    return db.query(models.Owner).offset(skip).limit(limit).all()

def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(name_surename = owner.name_and_surename, birth = owner.date_of_birth, 
    age = owner.age, insurence = owner.insurance)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def get_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()

def get_vehicles_by_year(db: Session, year: int):
    return db.query(models.Vehicle).filter(models.Vehicle.year == year).all()

def get_vehicles_by_type(db:Session, type: str):
    return db.query(models.Vehicle).filter(models.Vehicle.type_of_vehicle == type).all()

def get_vehicles_by_brand(db: Session, brand: str):
    return db.query(models.Vehicle).filter(models.Vehicle.vehicle_brand == brand).all()

def get_vehicles(db: Session, skip: int = 0 , limit: int = 15):
    return db.query(models.Vehicle).offset(skip).limit(limit).all()

def create_owner_vehicle(db: Session, vehicle: schemas.VehicleCreate, owner_id: int):
    db_vehicle = models.Vehicle(**vehicle.model_dump(),  owner_id = owner_id) 
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def re_registration_owner(db: Session, id: int, update_data: schemas.OwnerBase):
    owner = db.query(models.Owner).filter(models.Owner.owner_id == id).first()
    owner.name_and_surename = update_data
    owner.age = update_data.age
    owner.dat_of_birth = update_data.date_of_birth
    owner.insurance = update_data.insurance
    db.commit()
    db.refresh(owner)
    return owner
    
def del_owner(db: Session, owner: schemas.Owner):
    db.delete(owner)
    db.refresh()
