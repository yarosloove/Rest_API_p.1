import datetime

import config
from sqlalchemy import Integer, String, Float, DateTime, func
from sqlalchemy.ext.asyncio import (create_async_engine,
                                    async_sessionmaker, AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase, mapped_column, MappedColumn, Mapped


engine = create_async_engine(config.PG_DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):

    @property
    def id_dict(self):
        return {"id": self.id}


class Adv(Base):

    __tablename__ = "advertisement"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String, index=True)
    description:Mapped[str] = mapped_column(String, index=True)
    price: Mapped[float] = mapped_column(Float, index=True)
    author:Mapped[str] = mapped_column(String, index=True)
    date_of_creation:Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )


    @property
    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "author": self.author,
            "date_of_creation": self.date_of_creation
        }

async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def close_orm():
    await engine.dispose()

ORM_OBJ = Adv
ORM_CLS = type[Adv]