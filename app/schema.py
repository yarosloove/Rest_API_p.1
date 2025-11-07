import datetime

from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: float
    author: str



class GetAdvResponse(BaseModel):
    title: str
    description: str
    price: float
    author: str
    date_of_creation: datetime.datetime


class SearchAdvResponse(BaseModel):
    results: list[GetAdvResponse]


class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    author: str | None = None