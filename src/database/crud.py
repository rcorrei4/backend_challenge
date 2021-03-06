from sqlalchemy.orm import Session
from fastapi import HTTPException

from .func import criar_event_launch
from . import models
from src.schemas import schemas

def get_article(db: Session, article_id: int):
    return db.query(models.Articles).filter(models.Articles.id == article_id).first()

def get_articles(db: Session, page_size: int, page_index: int):
    #Envia os artigos ordenando por id podendo ter limite de resultado.
    return db.query(models.Articles).order_by(models.Articles.id.desc()).limit(page_size).offset((page_index-1)*page_size).all()


def create_article(db: Session, article: schemas.ArticleIn):

    #Cria um object com os dados recebidos do schema
    db_article = models.Articles(featured=article.featured, title=article.title, url=article.url,
                                imageUrl=article.imageUrl, newsSite=article.newsSite, summary=article.summary,
                                publishedAt=article.publishedAt)

    #Adiciona no banco de dados
    db.add(db_article)
    db.commit()

    #Caso tenha events ou launches adiciona dentro do objeto artigo
    if article.events:
        criar_event_launch("events", article, db_article, db)
    if article.launches:
        criar_event_launch("launches", article, db_article, db)

    db.commit()
    return db_article

def change_article(db: Session, article_id: int, article: schemas.ArticleIn):
    db_article = db.query(models.Articles).filter(models.Articles.id == article_id).first()

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    #Substitui os dados do artigo
    db_article.featured = article.featured
    db_article.title = article.title
    db_article.url = article.url
    db_article.imageUrl = article.imageUrl
    db_article.newsSite = article.newsSite
    db_article.summary = article.summary
    db_article.publishedAt = article.publishedAt

    #Adiciona no banco de dados
    db.add(db_article)
    db.commit()

    #Caso tenha events ou launches substitui os presentes dentro do objeto artigo
    if article.events:
        db_article = criar_event_launch("events", article, db_article, db)
    if article.launches:
        db_article = criar_event_launch("launches", article, db_article, db)

    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = db.query(models.Articles).filter(models.Articles.id == article_id).first()
    db.delete(db_article)
    db.commit()
    return {'Deleted'}

def get_last_article(db: Session):
    last_article = db.query(models.Articles).order_by(models.Articles.id.desc()).first()
    
    return last_article