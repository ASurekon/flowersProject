from fastapi import FastAPI
from routers.flowers import router as flowers_router
from routers.payment import router as payment_router
from database import engine
from models import Base

app = FastAPI()


app.include_router(flowers_router)
app.include_router(payment_router)

@app.on_event("startup")
async def startup_event():
    # Создание таблиц при старте (временное решение)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# @app.get("/")
# def hello_world():
#     return {"hello": "world"}