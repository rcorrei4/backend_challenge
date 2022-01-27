import os
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from core.database import crud
from core.models import models
from core.schemas import schemas
from core.database.settings import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def welcome():
    return {'Back-end Challenge 2021  - Space Flight News'}

@app.get("/articles/", response_model=list[schemas.Article])
async def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    articles = crud.get_articles(db, skip=skip, limit=limit)

    return articles

@app.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=article_id)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    return db_article

@app.put("/articles/{article_id}", response_model=schemas.Article)
async def change_article(article_id: int, article: schemas.ArticleIn, db: Session = Depends(get_db)):
    db_article = crud.change_article(db, article_id=article_id, article=article)

    return db_article

@app.post("/articles/", response_model=schemas.Article)
async def create_article(article: schemas.ArticleIn, db: Session = Depends(get_db)):
    
    return crud.create_article(db=db, article=article)

@app.delete("/articles/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id=article_id)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    return db_article
