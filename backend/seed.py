from .database import SessionLocal, engine, Base
from .models import Product

Base.metadata.create_all(bind=engine)

products = [
    # Headphones
    Product(name="SoundMax Pro", category="headphones", price=2499, rating=4.5,
            description="Wireless over-ear headphones with 40-hour battery life and ANC."),
    Product(name="AudioBeat Lite", category="headphones", price=1799, rating=4.2,
            description="Lightweight wireless headphones with 30-hour battery life."),
    Product(name="BassPro X1", category="headphones", price=2999, rating=4.6,
            description="Deep bass wireless headphones with ANC and 50-hour battery life."),
    Product(name="SonicPods Air", category="headphones", price=1499, rating=4.1,
            description="Compact wireless earbuds with a charging case."),
    Product(name="StudioSound 500", category="headphones", price=3999, rating=4.7,
            description="Over-ear studio headphones with balanced audio."),
    Product(name="TuneFlex Wireless", category="headphones", price=2199, rating=4.3,
            description="Flexible wireless headphones with a built-in microphone."),

    # Smartphones
    Product(name="TechPhone A1", category="smartphone", price=18999, rating=4.3,
            description="Smartphone with 8GB RAM and a 5000mAh battery."),
    Product(name="TechPhone Pro", category="smartphone", price=27999, rating=4.6,
            description="Performance-focused smartphone with AMOLED display."),
    Product(name="PixelNova 5G", category="smartphone", price=22999, rating=4.4,
            description="5G smartphone with a high-resolution camera."),
    Product(name="SmartOne Lite", category="smartphone", price=12999, rating=4.1,
            description="Budget smartphone with 6GB RAM and 128GB storage."),
    Product(name="UltraView X", category="smartphone", price=34999, rating=4.7,
            description="Premium smartphone with a 120Hz AMOLED display."),
    Product(name="PowerCell M2", category="smartphone", price=15999, rating=4.2,
            description="Smartphone with a large battery and fast charging."),

    # Laptops
    Product(name="CodeBook 15", category="laptop", price=54999, rating=4.4,
            description="Laptop suitable for programming and everyday work."),
    Product(name="CodeBook Air", category="laptop", price=62999, rating=4.7,
            description="Lightweight laptop with fast SSD storage."),
    Product(name="GameCore 16", category="laptop", price=79999, rating=4.5,
            description="Gaming laptop with dedicated graphics."),
    Product(name="StudyMate 14", category="laptop", price=42999, rating=4.2,
            description="Affordable laptop for students and office work."),
    Product(name="CreatorBook Pro", category="laptop", price=94999, rating=4.8,
            description="High-performance laptop for creative workloads."),
    Product(name="WorkStation Z", category="laptop", price=69999, rating=4.6,
            description="Powerful laptop for multitasking and development."),

    # Keyboards
    Product(name="KeyMaster K1", category="keyboard", price=2499, rating=4.5,
            description="Mechanical keyboard with tactile switches."),
    Product(name="TypePro Mini", category="keyboard", price=1799, rating=4.2,
            description="Compact wireless keyboard for everyday use."),
    Product(name="RGBStrike K2", category="keyboard", price=3299, rating=4.6,
            description="Mechanical gaming keyboard with RGB lighting."),
    Product(name="OfficeType 100", category="keyboard", price=899, rating=4.0,
            description="Affordable wired keyboard for office work."),
    Product(name="KeyFlex Wireless", category="keyboard", price=2199, rating=4.4,
            description="Wireless keyboard with comfortable low-profile keys."),
    Product(name="ProGamer TKL", category="keyboard", price=3999, rating=4.7,
            description="Tenkeyless mechanical keyboard for gaming."),

    # Mice
    Product(name="SpeedMouse M1", category="mouse", price=1299, rating=4.4,
            description="Ergonomic wireless mouse for everyday use."),
    Product(name="GameMouse X", category="mouse", price=2199, rating=4.6,
            description="Gaming mouse with adjustable DPI."),
    Product(name="ClickPro Basic", category="mouse", price=499, rating=4.0,
            description="Simple wired mouse for office and home use."),
    Product(name="Precision M5", category="mouse", price=1799, rating=4.5,
            description="Precision wireless mouse with adjustable sensitivity."),
    Product(name="RGBStrike Mouse", category="mouse", price=2499, rating=4.6,
            description="Gaming mouse with RGB lighting and programmable buttons."),
    Product(name="TravelMouse S", category="mouse", price=999, rating=4.2,
            description="Compact portable wireless mouse for laptops."),

    # Smartwatches
    Product(name="FitWatch Neo", category="smartwatch", price=2499, rating=4.2,
            description="Smartwatch with activity tracking and notifications."),
    Product(name="PulseTrack Pro", category="smartwatch", price=4999, rating=4.5,
            description="Smartwatch with GPS and multiple sports modes."),
    Product(name="TimeFit Active", category="smartwatch", price=3299, rating=4.3,
            description="Fitness smartwatch with a bright display."),
    Product(name="WatchLite S", category="smartwatch", price=1799, rating=4.0,
            description="Entry-level smartwatch with basic fitness features."),

    # Monitors
    Product(name="ViewMax 24", category="monitor", price=8999, rating=4.4,
            description="24-inch Full HD monitor for work and entertainment."),
    Product(name="UltraView 27", category="monitor", price=14999, rating=4.6,
            description="27-inch QHD monitor with a 100Hz refresh rate."),
    Product(name="GameScreen 24G", category="monitor", price=11999, rating=4.5,
            description="24-inch gaming monitor with a 165Hz refresh rate."),
    Product(name="OfficeDisplay 22", category="monitor", price=6999, rating=4.1,
            description="22-inch Full HD monitor for everyday office use."),
]

def seed_database():
    db = SessionLocal()

    try:
        db.query(Product).delete()
        db.add_all(products)
        db.commit()
        print(f"Successfully seeded {len(products)} products.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()