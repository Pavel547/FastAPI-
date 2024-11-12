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
#     disabled: str | None = None
    
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
    
# from typing import Annotated
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel

# fake_db = {
#     "user1": {
#         "username": "user1",
#         "full_name": "Alex Salewa",
#         "email": "qwerty1234@gmail.com",
#         "hashed_password": "fakehashedsecret1",
#         "disabled": False,
#     },
    
#     "user2": {
#         "username": "user2", 
#         "full_name": "Jhon Doe",
#         "email": "zxcvbn5678@gmail.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True,
#     }
# }

# app = FastAPI()

# def fake_hash_password(password: str):
#     return "fakehashed" + password

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# class User(BaseModel):
#     username:str
#     full_name: str | None = None
#     email: str | None = None
#     disabled: bool | None = None
    
# class UserInDB(User):
#     hashed_password: str | None = None 
        
# def get_user(db, username:str ):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def fake_docode_token(token):
#     # This doesn't provide any security at all
#     # Check the next version
#     user = get_user(fake_db, token)
#     return user

# def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_docode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user

# def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Invalid username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Invalid username or password")
    
#     return{"access_token": user.username, "token_type": "bearer"}

# @app.get("/users/me", response_model=User)
# async def read_user_me(
#     current_user: Annotated[User, Depends(get_current_active_user)]
#     ):
#     return current_user


# OAuth2 with Password (and hashing), Bearer with JWT tokens

from datetime import datetime, timedelta, timezone
from typing import Annotated
import os 
from dotenv import load_dotenv

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

load_dotenv()

SECRET_KEY = os.getenv("SECRETKEY")
ALGORITHM  = os.getenv("ALGORITHMHESHIN")
ACCESS_TOKEN_EXPIRE_MINUTES = int(("TIMEFORACCESS"))

fake_db = {
    "user1":{
        "username": "user1",
        "full_name": "Jhon Doe",
        "email": "tester@test.com",
        "hashed_passwoed": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}
