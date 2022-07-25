import sys
from fastapi import FastAPI, status
import models
#import schemas
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



