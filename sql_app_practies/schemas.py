from pydantic import BaseModel
from datetime import date

class VechicleBase(BaseModel):
    vechicle_plate: str
    type_of_vechicle: str
    vechicle_mark: str
    year: date
    date_of_registration: date
    
class VechicleCreate(VechicleBase):
    pass

class Vechicle(VechicleBase):
    vechicle_id: int

class OwnerBase(BaseModel):
    name_and_surename: str
    date_of_birth: date

    
class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    owner_id: int
    insurance: bool
    vechicles: list[Vechicle] = []

    