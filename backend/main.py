from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from .database import engine, Base, SessionLocal
from . import models

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "AI Commerce Agent")

def get_db():
    db = SessionLocal()

    try:
        yield db 

    finally:
        db.close()

        
@app.get("/")
def root():
    return {"message" : "AI Commerce is running "}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()

    return products
