from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence

# Konfiguracja bazy danych
DATABASE_URL = "postgresql+asyncpg://user:password@db/coffee_shop"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Definicja modelu ORM
class Coffee(Base):
    __tablename__ = "coffees"
    id = Column(Integer, Sequence("coffee_id_seq"), primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

# Tworzenie aplikacji FastAPI
app = FastAPI()

# Tworzenie tabel w bazie danych
engine = create_async_engine(DATABASE_URL, echo=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await init_db()

# Dependency do sesji bazy danych
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Endpointy (bez logiki biznesowej)
@app.get("/coffees/")
async def get_coffees(db: AsyncSession = Depends(get_db)):
    pass

@app.post("/coffees/", status_code=201)
async def add_coffee(coffee_data: dict, db: AsyncSession = Depends(get_db)):
    pass

@app.get("/coffees/{coffee_id}")
async def get_coffee_by_id(coffee_id: int, db: AsyncSession = Depends(get_db)):
    pass