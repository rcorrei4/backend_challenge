from sqlalchemy.orm import Session

import models, schemas


def get_article(db: Session, article_id: int):
    return db.query(models.Articles).filter(models.Articles.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Articles).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleIn):
    db_article = models.Articles(featured=article.featured, title=article.title, url=article.url,
                                imageUrl=article.url, newsSite=article.newsSite, summary=article.summary,
                                publishedAt=article.publishedAt)

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    if article.events:
        db_event = models.Events(id=article.events[0].id, provider=article.events[0].provider)
        db_article.events.append(db_event)
        db.add(db_event)
        db.commit()
        db.refresh(db_article)
        db.refresh(db_event)

    if article.launches:
        db_launches = models.Launches(id=article.launches[0].id, provider=article.launches[0].provider)
        db_article.launches.append(db_launches)
        db.add(db_launches)
        db.commit()
        db.refresh(db_article)
        db.refresh(db_launches)

    return db_article

def delete_article(db: Session, article_id: int):
    db_article = db.query(models.Articles).filter(models.Articles.id == article_id).first()
    db.delete(db_article)
    db.commit()
    return {'Deleted'}