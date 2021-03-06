import os
import asyncio
from fastapi import Depends, FastAPI, HTTPException
from apscheduler.schedulers.background import BackgroundScheduler

from .database import models
from .routes import articles as article_routes
from .database.settings import SessionLocal, engine
from .cron import check_articles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(article_routes.router)

@app.get("/", status_code=200)
async def welcome():
    return {'Back-end Challenge 2021 🏅 - Space Flight News'}

@app.on_event('startup')
async def update_article():
    scheduler = BackgroundScheduler(timezone="America/Sao_Paulo")
    scheduler.add_job(check_articles, 'cron', hour=9)
    scheduler.start()