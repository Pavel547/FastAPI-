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

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = {
    "johndoe":{
        "username": "johndoe",
        "full_name": "Jhon Doe",
        "email": "tester@test.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    disabled: bool | None = None
    
class UserInDB(User):
    hashed_password: str
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_paswword, hashed_password):
    return pwd_context.verify(plain_paswword, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_acces_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_db, username=token_data.username)
    if user is None:
        raise create_acces_token
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_acces_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acces_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    acces_token = create_acces_token(
        data={"sub": user.username}, expires_delta=acces_token_expire
    )
    return Token(access_token=acces_token, token_type="bearer")

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

@app.get("/users/me/items/")
async def read_user_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user}]
