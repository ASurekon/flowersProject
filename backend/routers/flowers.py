from fastapi import APIRouter
from fastapi.params import Depends
from database import get_db
from models import Flower
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


router = APIRouter(prefix="/flowers")




@router.get("/")
async def get_all_flowers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Flower).where(Flower.available == True))
    if result:
        return result.scalars().all()
    else:
        return "тут еще пока нет ничего долбаеб"