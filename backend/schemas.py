
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class PaymentBase(BaseModel):
    pass


class PaymentCreate(PaymentBase):
    customer_phone: str
    customer_email: str
    customer_name: str
    # flower_id: int


class PaymentInDB(PaymentCreate):
    flower_id: int
    paid: bool = False
    given_out: bool = False
    closed: bool = False


class FlowerBase(BaseModel):
    title: str
    price: float
    photo_url: str

class FlowerCreate(FlowerBase):
    pass

class FlowerInDB(FlowerCreate):
    available: bool = True

class FlowerUpdate(BaseModel):
    available: Optional[bool] = None
    price: Optional[float] = None