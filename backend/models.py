from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from database import Base

class Flower(Base):
    __tablename__ = "flowers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    photo_url = Column(String, unique=True, index=True)
    price = Column(Float)
    available = Column(Boolean, default=True)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    customer_phone = Column(String, index=True)
    customer_email = Column(String, index=True)
    customer_name = Column(String, index=True)
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    paid = Column(Boolean, default=False)
    given_out = Column(Boolean, default=False)
    closed = Column(Boolean, default=False)