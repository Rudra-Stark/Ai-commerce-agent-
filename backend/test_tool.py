from .database import SessionLocal 
from .tools import search_products

db = SessionLocal()

try:
    products = search_products(
        db = db,
        category = "headphones",
        max_price = 3000
    )
    for product in products:
        print(product["name"], "-" , product["price"], "-" , product["rating"])

finally:
    db.close()