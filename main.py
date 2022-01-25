from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "postgresql://huvhufwahvlxqy:73c730df4555a68870cabb2be044e3d40488681089db7512d75fcd5e3458fea1@ec2-18-209-169-66.compute-1.amazonaws.com:5432/d7tou3tlqd94di"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

articles = sqlalchemy.Table(
    "articles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("featured", sqlalchemy.Boolean),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("imageUrl", sqlalchemy.String),
    sqlalchemy.Column("newsSite", sqlalchemy.String),
    sqlalchemy.Column("summary", sqlalchemy.String),
    sqlalchemy.Column("publishedAt", sqlalchemy.String),
    sqlalchemy.Column("launches", sqlalchemy.Integer, sqlalchemy.ForeignKey('launches.id')),
    sqlalchemy.Column("events", sqlalchemy.Integer, sqlalchemy.ForeignKey('events.id')),
)

launches = sqlalchemy.Table(
    "launches",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("provider", sqlalchemy.String),
)

events = sqlalchemy.Table(
    "events",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("provider", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)

class LaunchesIn(BaseModel):
    provider: str

class Launches(BaseModel):
    id: int
    provider: str

class EventsIn(BaseModel):
    provider: str

class Events(BaseModel):
    id: int
    provider: str


class ArticleIn(BaseModel):
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str

class Article(BaseModel):
    id: int
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def welcome():
    return {"Back-end Challenge 2021  - Space Flight News"}


@app.get("/articles/", response_model=List[Article])
async def read_articles():
    query = articles.select()
    return await database.fetch_all(query)

@app.post("/articles/", response_model=Article)
async def create_articles(article: ArticleIn):
    query = articles.insert().values(featured=article.featured, title=article.title, 
                                    url=article.url, imageUrl=article.imageUrl,
                                    newsSite=article.newsSite, summary=article.summary,
                                    publishedAt=article.publishedAt)

    last_record_id = await database.execute(query)
    return {**article.dict(), "id": last_record_id}