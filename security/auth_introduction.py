# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_schema)]):
#     return {"token": token}

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
    
    
from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel

fake_user_db = {
    "johndoe" : {
        "username": "johndoe",
        "fullname": "John Doe",
        "email": "johndoe@gmail.com",
        "password": "fakehashedsecret",
        "disable": False,
    },
    
    "alexi": {
        "username": "alexi",
        "fullname": "Alex Wershpe",
        "email": "alexi@gmail.com",
        "password": "fakehashedsecret2",
        "disable": True,
    }
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_shema = OAuth2PasswordBearer(tokenUrl="token")


