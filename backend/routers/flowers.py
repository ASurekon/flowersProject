from typing import Annotated
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from database import get_db
from models import Flower
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from schemas import FlowerUpdate


router = APIRouter(prefix="/flowers", tags=["Flowers"])




@router.get("/")
async def get_all_flowers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Flower).where(Flower.available == True).order_by(Flower.id))
    if result:
        return result.scalars().all()
    else:
        return "тут еще пока нет ничего"


@router.patch("/update/{card_id}")
async def update_card(card_id: int, update_data: Annotated[FlowerUpdate, Depends()], db: AsyncSession = Depends(get_db)):
    data_to_update = update_data.model_dump(exclude_defaults=True)
    card = await db.execute(select(Flower).where(Flower.id == card_id))
    card_to_update = card.scalar_one_or_none()
    for field, value in data_to_update.items():
        setattr(card_to_update, field, value)
    db.add(card_to_update)
    await db.commit()
    await db.refresh(card_to_update)
    return card_to_update



@router.delete('/delete/{card_id}')
async def delete_card(card_id: int, db: AsyncSession = Depends(get_db)):
    flower_card = await db.execute(select(Flower).where(Flower.id == card_id))
    flower_card_db = flower_card.scalar_one_or_none()
    if flower_card_db:
        await db.delete(flower_card_db)
        await db.commit()
    else:
        raise HTTPException(status_code=404, detail="Card not found or you don't have enough permissions to do that")
    return "Deleting completed successfully"