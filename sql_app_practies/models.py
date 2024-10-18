from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Owner(Base):
    __tablename__ = "owners"
    owner_id = Column(Integer, primary_key=True, index=True)
    name_and_surename = Column(String, index=True)
    gender = Column(String)
    insurance = Column(Boolean, default=False)
    
    vehicle = relationship("Vehicle", back_populates="owner")
    
    
    
class Vehicle(Base):
    __tablename__ = "vehicles"
    vechicle_id = Column(Integer, primary_key=True, index=True)
    vechicle_number = Column(String, index=True)
    type_of_vehicle = Column(String)
    vechicle_mark = Column(String)
    year = Column(Integer)
    date_of_registr = Column(Date)
    owner_id = Column(Integer, ForeignKey("owner_id"))
    
    owner = relationship("Owner", back_populates="vehicle")
    