from fastapi import FastAPI
# from enum import Enum

app = FastAPI()

# @app.get('/')
# async def root():
#     return {"message :": "Hello world"}

# Path Parameters

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/congratulations/{name}")
# async def congrat_user(name):
#     return {"Congratulations you finishe the school": name}


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
    
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# Query Parameters

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# @app.get("/items/")
# async def red_item(skip: int=0, limit: int=5):
#     return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# Mini practies
# @app.get("/users/{user_name}")
# async def read_item(user_name: str, q: str | None = None, active: bool | None = None):
#     user= {"user_name": user_name}
    
#     if active is True:
#         user.update({"active": "user is active now"})
#     if active is False:
#         user.update({"active": "user in inactive now"})
        
#     return user

# Query parameter type conversion

# @app.get("/items/{item_id}")
# async def read_iteme(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
    
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
    
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item

# Practies

# @app.get("/")
# async def root():
#     return {"message": "Hello admin"}

# @app.get("/users/{user_name}")
# async def return_user(user_name: str, user_id: int | None = None):
#     return {"user_name": user_name, "user_id": user_id}


# @app.get("/items/{item_id}/itmname/{item_name}")
# async def read_item(item_id: int, item_name: str, quantity: int | None = None):
#     if quantity:
#         return {"item_id": {item_id}, "itmname": {item_name}, "quantity": {quantity}}
#     else:
#         return {"item_id": {item_id}, "itmname":{item_name}}


@app.get("/user/{user_name}")
async def hello_user(user_name: str,):
    return {"message": "Hello", "name": user_name}
