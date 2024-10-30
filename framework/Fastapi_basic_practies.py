from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello this is basic practies with fastapi"}

@app.get("/hello_user/{user_name}")
def hello(user_name: str):
    return {"message:": "Hello", "name:": user_name}
