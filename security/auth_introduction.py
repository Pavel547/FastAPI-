# this is the First Steps to authorized

# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_schema)]):
#     return {"token": token}

# this is the code which Get Current User but its only example he is not working 

# from typing import Annotated

# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer("token")

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     fullname: str | None = None
#     disable: str | None = None
    
# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecode", email="testemail@gmail.com", fullname="Tester test"
#     )

# async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
#     user = fake_decode_token(token)
#     return user

# @app.get("/users/me")
# async def read_users_me(current_user: Annotated[str, Depends(oauth2_schema)]):
#     return current_user
  
#   
    
from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "Alex Naja",
        "email": "test1@gmail.com",
        "password": "fakehashedpassword1",
        "disabled": False,
    },
    
    "user2": {
        "username": "user2",
        "full_name": "Oleg Brovsky",
        "email": "test2@gmail.com",
        "password": "fakehashedpassword2",
        "disable": True,
    },
}

app = FastAPI()

def fakr_hash_password(password: str):
    return "fakehashed" + password

oauth2_schema = OAuth2PasswordBearer("token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: bool | None = None
    
class UserInDB(User):
    password: str
