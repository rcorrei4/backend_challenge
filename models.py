from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    featured = Column(Boolean)
    title = Column(String)
    url = Column(String)
    imageUrl = Column(String)
    newsSite = Column(String)
    summary = Column(String)
    publishedAt = Column(String)

    launches = relationship("Launches")
    events = relationship("Events")


class Launches(Base):
    __tablename__ = "launches"

    id = Column(String, primary_key=True, index=True)
    provider = Column(String)

    article_id = Column(Integer, ForeignKey('articles.id'))

class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, index=True)
    provider = Column(String)

    article_id = Column(Integer, ForeignKey('articles.id'))