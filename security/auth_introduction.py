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

class User(BaseModel):
    username: str
    fullname: str | None = None
    email:str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashedpassword: str
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_user_db, token)
    return user
    
async def get_current_user(token: Annotated[str, Depends(oauth2_shema)]):
    user = fake_decode_token(token)
    
    if user is None:
        raise HTTPException (
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password or username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(oauth2_shema)]
):
    if current_user.disabled:
        raise HTTPException (status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_user_db.get(form_data.username)
    if user_dict is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {"acces_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

