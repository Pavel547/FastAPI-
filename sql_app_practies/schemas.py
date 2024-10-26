from pydantic import BaseModel, field_validator
from datetime import date

class VehicleBase(BaseModel):
    vehicle_plate: str
    type_of_vehicle: str
    vehicle_brand: str
    year: int
    date_of_registration: date
    
    @field_validator('year')
    def validator_for_year(cls, value):
        today = date.today()
        if value > today.year:
            raise ValueError("The year of manufacture cannot be greater than the current date")
        return value
    
    @field_validator('date_of_registration')
    def validator_for_registration(cls, value):
        if value > date.today():
            raise ValueError("The vehicle's registration date cannot exceed today's date")
        return value
    
class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    vehicle_id: int
    owner_id: int
    
    class Config:
        from_attributes = True

class OwnerBase(BaseModel):
    name_and_surename: str
    date_of_birth: date
    age: int
    insurance: bool
    
    @field_validator('age')
    def validator_for_age(cls, value):
        if value < 18:
            raise ValueError("The minimum age for driving a car is 18 years")
        return value
    
    @field_validator('date_of_birth')
    def validator_for_date_birth(cls, value):
        if value > date.today():
            raise ValueError("The registration date cannot be in the future")
        return value

class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    owner_id: int
    vehicles: list[Vehicle] = []
    
    class Config:
        from_attributes = True
