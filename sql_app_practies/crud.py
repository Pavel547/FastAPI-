from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Owner).filter(models.Owner.owner_id == user_id).first()

def get_users_by_age(db:Session, age: int):
    return db.query(models.Owner).filter(models.Owner.age == age).all()

def get_users(db: Session, skip: int = 0, limit: int = 15):
    return db.query(models.Owner).offset(skip).limit(limit).all()

def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(name_surename = owner.name_and_surename, birth = owner.date_of_birth, 
    age = owner.age, insurence = owner.insurance)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def get_vechicle_by_id(db: Session, vechicle_id: int):
    return db.query(models.Vechicle).filter(models.Vechicle.vechicle_id == vechicle_id).first()

def get_vechicles_by_year(db: Session, year: int):
    return db.query(models.Vechicle).filter(models.Vechicle.year == year).all()

def get_vechicles_by_type(db:Session, type: str):
    return db.query(models.Vechicle).filter(models.Vechicle.type_of_vechicle == type).all()

def get_vechicles_by_mark(db: Session, mark: str):
    return db.query(models.Vechicle).filter(models.Vechicle.vechicle_mark == mark).all()

def get_vechicles(db: Session, skip: int = 0 , limit: int = 15):
    return db.query(models.Vechicle).offset(skip).limit(limit).all()

def create_vechicle(db: Session, vechicle: schemas.VechicleCreate):
    db_vechicle = models.Vechicle(plate_number = vechicle.vechicle_plate, type = vechicle.type_of_vechicle,
    mark = vechicle.vechicle_mark, made = vechicle.year, date_of_registration = vechicle.date_of_registration)
    db.add(db_vechicle)
    db.commit()
    db.refresh(db_vechicle)
    return db_vechicle

