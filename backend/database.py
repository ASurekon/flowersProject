import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
# DATABASE_URL=os.getenv("DATABASE_URL")

# SQLALCHEMY_DATABASE_URL = DATABASE_URL
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,

)

AsyncSessionLocal = sessionmaker(
    engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


# async def create_all_tables():
#     try:
#         print("Creating all tables...")
#         async with engine.begin() as conn:
#             await conn.run_sync(Base.metadata.drop_all)  # Осторожно: удаляет все данные!
#             await conn.run_sync(Base.metadata.create_all)
#         print("✅ All tables created successfully!")
#     except Exception as e:
#         print(f"❌ Error creating tables: {e}")
        

# if __name__ == "__main__":
#     asyncio.run(create_all_tables())