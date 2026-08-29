from fastapi import FastAPI
from .database import engine, Base
from . import models

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "AI Commerce Agent")

@app.get("/")
def root():
    return {"message" : "AI Commerce is running "}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
