from fastapi import FastAPI, Query
from sqlalchemy import select, and_
from pydantic import BaseModel
from lifespan import lifespan
from dependency import SessionDependency
from models import Adv
import models
import crud
import datetime
from schema import (
    CreateAdvRequest, IdResponse, GetAdvResponse, SearchAdvResponse,
    UpdateAdvRequest
)

app = FastAPI(
    title="Adv API",
    terms_of_service="",
    description="list of advertisement",
    lifespan=lifespan
)

@app.post("/advertisement", response_model=IdResponse)
async def create_adv(session: SessionDependency, item: CreateAdvRequest):
    adv = Adv(
        title = item.title,
        description = item.description,
        price = item.price,
        author = item.author
    )
    await crud.add_item(session, adv)
    return adv.id_dict

@app.get("/advertisement/{advertisement_id}", response_model=GetAdvResponse)
async def get_adv(session: SessionDependency, advertisement_id: int):
    adv = await crud.get_item_by_id(session, Adv, advertisement_id)
    return adv.dict

@app.get("/advertisement", response_model=SearchAdvResponse)
async def get_advertisement(session: SessionDependency,
                            title: str = None,
                            description: str = None,
                            author: str = None,
                            price: float = None):
    conditions = []
    if title:
        conditions.append(models.Adv.title == title)
    if description:
        conditions.append(models.Adv.description == description)
    if author:
        conditions.append(models.Adv.author == author)
    if price:
        conditions.append(models.Adv.price == price)
    query = select(models.Adv).where(and_(*conditions)).limit(10000)
    advertisements = await session.scalars(query)
    return {"results": [advertisement.dict for advertisement in advertisements]}

@app.patch("/advertisement/{advertisement_id}", response_model=IdResponse)
async def update_adv(session: SessionDependency, advertisement_id: int, item: UpdateAdvRequest):
    adv = await crud.get_item_by_id(session, Adv, advertisement_id)
    if item.title is not None:
        adv.title = item.title
    if item.description is not None:
        adv.description = item.description
    if item.price is not None:
        adv.price = item.price
    if item.author is not None:
        adv.author = item.author
        adv.date_of_creation = datetime.datetime.now()
    await crud.add_item(session, adv)
    return {"id": advertisement_id}

@app.delete("/advertisement/{advertisement_id}", response_model=IdResponse)
async def delete_adv(session: SessionDependency, advertisement_id: int):
    adv = await crud.get_item_by_id(session, Adv, advertisement_id)
    await crud.delete_item(session, adv)
    return {"id": advertisement_id}