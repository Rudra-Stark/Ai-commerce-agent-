from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models


def normalize_category(category):
    """
    Normalize category names and common synonyms.
    """

    if not category:
        return None

    category = category.strip().casefold()

    category_aliases = {
        # Headphones
        "headphone": "headphones",
        "headphones": "headphones",

        # Smartphones
        "mobile": "smartphone",
        "mobiles": "smartphone",
        "smartphone": "smartphone",
        "smartphones": "smartphone",
        "cell phone": "smartphone",
        "cell phones": "smartphone",

        # Laptops
        "laptop": "laptop",
        "laptops": "laptop",
        "notebook": "laptop",
        "notebooks": "laptop",

        # Keyboards
        "keyboard": "keyboard",
        "keyboards": "keyboard",

        # Mice
        "mouse": "mouse",
        "mice": "mouse",
    }

    return category_aliases.get(category, category)


def search_products(
    db: Session,
    category=None,
    max_price=None,
    min_rating=None
):
    """
    Search products using category, price and rating filters.
    """

    category = normalize_category(category)

    query = db.query(models.Product)

    # Case-insensitive category matching
    if category:
        query = query.filter(
            func.lower(models.Product.category) == category
        )

    # Maximum price filter
    if max_price is not None:
        query = query.filter(
            models.Product.price <= max_price
        )

    # Minimum rating filter
    if min_rating is not None:
        query = query.filter(
            models.Product.rating >= min_rating
        )

    products = query.all()

    # Convert SQLAlchemy objects into dictionaries
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
    """
    AI-friendly product search tool.

    This function is exposed to the AI model.
    It manages its own database session.
    """

    from .database import SessionLocal

    db = SessionLocal()

    try:
        return search_products(
            db=db,
            category=category,
            max_price=max_price,
            min_rating=min_rating
        )

    finally:
        db.close()