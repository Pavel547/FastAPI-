from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Owner(Base):
    __tablename__ = "owners"
    
    owner_id = Column(Integer, primary_key=True, index=True)
    name_and_surename = Column(String, index=True)
    age = Column(Integer, index=True)
    dat_of_birth = Column(Date)
    insurance = Column(Boolean, default=False)
    
    vehicles = relationship("Vehicle", back_populates="owner")
    
class Vehicle(Base):
    __tablename__ = "vehicles"
    
    vehicle_id = Column(Integer, primary_key=True, index=True)
    vehicle_plate = Column(String, index=True, unique=True)
    type_of_vehicle = Column(String(25))
    vehicle_brand = Column(String)
    year = Column(Integer, index=True)
    date_of_registration = Column(Date, index=True)
    owner_id = Column(Integer, ForeignKey("owners.owner_id"))
    
    owner = relationship("Owner", back_populates="vehicle")
    