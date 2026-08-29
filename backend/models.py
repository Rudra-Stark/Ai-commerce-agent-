from sqlalchemy import Column, Integer, String, Float
from .database import Base 

class Product(Base):                     # Base is what allows SQLAlchemy to recognize your Python class as a database model.
    __tablename__ = "products"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    category = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    rating = Column(Float)
    description = Column(String)
