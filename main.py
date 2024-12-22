# main.py
#########

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def call_hello_world():
    return {"message": "Hello World!"}

@app.get("/login")
def call_login():
    return {"message": "You reached the login endpoint"}