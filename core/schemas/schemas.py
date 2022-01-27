from pydantic import BaseModel
from typing import Optional

#Schemas "In" são necessários para post requests

class EventsIn(BaseModel):
    provider: str

class Events(BaseModel):
    id: str
    provider: str

    class Config:
        orm_mode = True

class LaunchesIn(BaseModel):
    provider: str

class Launches(BaseModel):
    id: str
    provider: str

    class Config:
        orm_mode = True

class ArticleIn(BaseModel):
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    launches: list[Events] = []
    events: list[Launches] = []

class Article(BaseModel):
    id: int
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    launches: list[Events] = []
    events: list[Launches] = []

    class Config:
        orm_mode = True