from typing import List

import databases
import sqlalchemy
import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel

class Launches(BaseModel):
    id: str
    provider: str

class Events(BaseModel):
    id: str
    provider: str

class Article(BaseModel):
    id:int
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    launches: list[Launches]
    events: list[Events]

app = FastAPI()

@app.get("/")
def home():
    return {"Back-end Challenge 2021  - Space Flight News"}


@app.get("/test/{article_id}")
def get_article(article_id: str):
    r = requests.get('https://api.spaceflightnewsapi.net/v3/articles/'+article_id)

    article = Article(**r.json())
    return article