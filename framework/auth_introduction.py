# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_schema)]):
#     return {"token": token}


from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_shema = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    fullname: str | None = None
    disable: bool | None = None
    
def fake_decode_token(token):
    return User(
        username=token + "fakedecode", email="testemail@gmail.com", fullname="Tester Test"
    )
    
async def get_current_user(token: Annotated[str, Depends(oauth2_shema)]):
    user = fake_decode_token(token)
    
@app.get("/users/me")
async def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
    
    
    