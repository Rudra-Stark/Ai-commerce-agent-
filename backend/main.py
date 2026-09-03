from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from .database import engine, Base, SessionLocal
from typing import Optional 
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
def get_products(
    category: Optional[str] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    db : Session = Depends(get_db)
):
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category == category)

    if max_price is not None:
        query = query.filter(models.Product.price <= max_price)

    if min_rating is not None:
        query = query.filter(models.Product.rating >= min_rating)

    products = query.all()
    return products 
