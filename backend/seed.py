from .database import SessionLocal, engine, Base
from .models import Product

Base.metadata.create_all(bind = engine)

products = [
    Product(
        name = "SoundMax Pro",
        category = "headphones",
        price = 2200,
        rating = 4.5,
        description = "Wireless over-ear headphones with 40-hour battery life and active noise cancellation. "
    ),
    Product(
        name = "AudioBeat Lite",
        category = "headphones",
        price = 1799,
        rating = 4.2,
        description = "LightWeight wireless headphones with 30-hour battery life and comfortable ear cushions. "
    ),
    Product(
        name = "TechPhone A1",
        category = "smartphone",
        price = 18999,
        rating = 4.6,
        description = "5G smartphone with a high-resolution camera, large display and all-day battery. "
    ),
]

def seed_database():
    db = SessionLocal()
    try:

        if db.query(Product).count() == 0:
            db.add_all(products)
            db.commit()
            print("Products added successfully!")

        else:
            print("Database already contains products.")

    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

    