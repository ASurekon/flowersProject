from typing import Annotated, Optional
from fastapi import APIRouter, Query, Depends 
from sqlalchemy import select
from enum import Enum
from database import get_db
from models import Flower, Payment
from schemas import PaymentCreate, PaymentUpdate
from sqlalchemy.ext.asyncio import AsyncSession



router = APIRouter(prefix="/order")


@router.post("/create_order/{card_id}")
async def create_order(
    card_id: int,
    payment_data: Annotated[PaymentCreate, Depends()],
    db: AsyncSession = Depends(get_db)
):

    card = await db.execute(select(Flower).where(Flower.id == card_id))
    db_card = card.scalar_one_or_none()
    if db_card:
        db_payment = Payment(
            flower_id=card_id,
            **payment_data.model_dump()
        )
        db.add(db_payment)
        await db.commit()
        await db.refresh(db_payment)
        return {"payment_data": db_payment,
                "price": db_card.price}
    return {"card": card.scalar_one_or_none(),
            "payment_data": payment_data}



@router.patch("/update_order_status/{payment_id}")
async def update_status(
    payment_id: int,
    update_data: Annotated[PaymentUpdate, Depends()],
    db: AsyncSession = Depends(get_db)
):
    
    updated = update_data.model_dump(exclude_defaults=True)
    payment = await db.execute(select(Payment).where(Payment.id == payment_id))
    db_payment = payment.scalar_one_or_none()
    
    for field, value in updated.items():
        setattr(db_payment, field, value)

    db.add(db_payment)
    await db.commit()
    await db.refresh(db_payment)
    return db_payment
