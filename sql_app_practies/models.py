from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Owner(Base):
    __tablename__ = "owners"
    
    owner_id = Column(Integer, primary_key=True, index=True)
    name_and_surename = Column(String, index=True)
    dat_of_birth = Column(Date)
    insurance = Column(Boolean, default=False)
    
    vechicles = relationship("Vechicle", back_populates="owner")
    
class Vechicle(Base):
    __tablename__ = "vechicles"
    
    vechicle_id = Column(Integer, primary_key=True, index=True)
    vechicle_plate = Column(String, index=True, unique=True)
    type_of_vechicle = Column(String(25))
    vechicle_mark = Column(String)
    year = Column(Integer, index=True)
    date_of_registration = Column(Date, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    
    owner = relationship("Owner", back_populates="vechicle")
    