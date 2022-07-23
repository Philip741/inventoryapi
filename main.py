import sys
from fastapi import FastAPI
from .database import SessionLocal, engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



