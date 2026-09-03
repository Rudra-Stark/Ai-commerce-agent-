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
    Product(
    name="CodeBook Air",
    category="Laptop",
    price=54999,
    rating=4.4,
    description="15-inch laptop with 16GB RAM and 512GB SSD, designed for programming and productivity."
    ),

    Product(
        name="CodeBook Pro",
        category="Laptop",
        price=74999,
        rating=4.7,
        description="14-inch high-performance laptop with 16GB RAM and 1TB SSD, ideal for developers and professionals."
    ),

    Product(
        name="TechMate X1",
        category="Laptop",
        price=62999,
        rating=4.5,
        description="15.6-inch laptop with Intel Core i5 processor, 16GB RAM and 512GB SSD for everyday work."
    ),

    Product(
        name="PixelBook Lite",
        category="Laptop",
        price=45999,
        rating=4.2,
        description="Lightweight 14-inch laptop with 8GB RAM and 512GB SSD, perfect for students and office work."
    ),

    Product(
        name="GameForce 15",
        category="Gaming Laptop",
        price=89999,
        rating=4.6,
        description="15.6-inch gaming laptop with powerful graphics, 16GB RAM and 1TB SSD for gaming and content creation."
    ),

    Product(
        name="UltraView 27",
        category="Monitor",
        price=18999,
        rating=4.5,
        description="27-inch Full HD IPS monitor with vibrant colors and a 100Hz refresh rate for work and entertainment."
    ),

Product(
    name="KeyPro Mechanical",
    category="Keyboard",
    price=3499,
    rating=4.4,
    description="Mechanical keyboard with RGB lighting, tactile switches and a comfortable design for programming and gaming."
),

Product(
    name="SpeedMouse X",
    category="Mouse",
    price=1999,
    rating=4.3,
    description="Wireless ergonomic mouse with adjustable DPI and long battery life for productivity and gaming."
),

Product(
    name="SoundPods Pro",
    category="Earbuds",
    price=4999,
    rating=4.5,
    description="Wireless earbuds with active noise cancellation, clear audio and up to 30 hours of battery life."
),

Product(
    name="BassMax 500",
    category="Headphones",
    price=6999,
    rating=4.6,
    description="Over-ear wireless headphones with deep bass, active noise cancellation and comfortable ear cushions."
),

Product(
    name="PowerBank Ultra",
    category="Power Bank",
    price=2499,
    rating=4.3,
    description="20000mAh power bank with fast charging and dual USB ports for smartphones and other devices."
),

Product(
    name="SmartWatch Fit",
    category="Smartwatch",
    price=5999,
    rating=4.4,
    description="Smartwatch with fitness tracking, heart-rate monitoring, sleep tracking and smartphone notifications."
),

Product(
    name="PhoneMax 5G",
    category="Smartphone",
    price=29999,
    rating=4.5,
    description="5G smartphone with a 6.6-inch AMOLED display, 128GB storage and a high-resolution camera."
),

Product(
    name="TabPro 11",
    category="Tablet",
    price=24999,
    rating=4.3,
    description="11-inch tablet with 8GB RAM and 128GB storage, suitable for studying, entertainment and productivity."
),

Product(
    name="WebCam HD Pro",
    category="Webcam",
    price=2999,
    rating=4.2,
    description="1080p webcam with built-in microphone, autofocus and wide-angle lens for online meetings and streaming."
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

    