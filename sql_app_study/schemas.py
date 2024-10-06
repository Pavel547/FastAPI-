from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class UserBase(BaseModel):
    email: str

    
class UserCreate(UserBase):
    password: str