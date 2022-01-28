from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas import schemas
from src.database import crud
from src.database.settings import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={403: {"description": "Forbidden"}},
)

@router.get("/articles/", response_model=list[schemas.Article])
async def read_articles(page_limit: int = 10, page_index: int = 1, db: Session = Depends(get_db)):

    articles = crud.get_articles(db, page_size=page_limit, page_index=page_index)

    return articles

@router.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=article_id)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    return db_article

@router.put("/articles/{article_id}", response_model=schemas.Article)
async def change_article(article_id: int, article: schemas.ArticleIn, db: Session = Depends(get_db)):
    db_article = crud.change_article(db, article_id=article_id, article=article)

    return db_article

@router.post("/articles/", response_model=schemas.Article)
async def create_article(article: schemas.ArticleIn, db: Session = Depends(get_db)):
    
    return crud.create_article(db=db, article=article)

@router.delete("/articles/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id=article_id)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    return db_article