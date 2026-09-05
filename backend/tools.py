from sqlalchemy.orm import Session 
from . import models

def search_products(
        db: Session,
        category = None,
        max_price = None,
        min_rating = None
):
    query = db.query(models.Product)

    if category:
        query = query.filter(models.Product.category == category)

    if max_price is not None:
        query = query.filter(models.Product.price <= max_price)

    if min_rating is not None:
        query = query.filter(models.Product.rating >= min_rating)

    products = query.all()
    return [
        {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "rating": product.rating,
            "description": product.description 
        }
        for product in products
    ]

def search_products_for_ai(
        category: str = None,
        max_price: float = None,
        min_rating: float = None
):
    from .database import SessionLocal
    db = SessionLocal()

    try:
        return search_products(
            db = db,
            category = category,
            max_price = max_price,
            min_rating = min_rating
        )
    finally:
        db.close()