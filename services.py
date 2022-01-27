import requests
from fastapi import Depends
from sqlalchemy.orm import Session

from core.models import models
from core.schemas import schemas
from core.database.settings import SessionLocal

# Dependency
db = SessionLocal()

articles_count = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles/count")

articles = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles", params={"_limit": articles_count})

def criar_event_launch(event_launch, article, db_article, db):
	if event_launch == "events":
		event_id = str(article['events'][0]['id'])

		#Caso já exista um objeto launches com o id adiciona o mesmo, se não, cria um objeto
		if db.query(models.Events).filter(models.Events.id == event_id).first() is not None:
			db_event = db.query(models.Events).filter(models.Events.id == event_id).first()
			db_article.events.append(db_event)
		else:
			db_event = models.Events(id=event_id, provider=article['events'][0]['provider'])
			db_article.events.append(db_event)

			#Adiciona no banco de dados
			db.add(db_event)
		
	if event_launch == "launches":
		#Caso já exista um objeto launches com o id adiciona o mesmo, se não, cria um objeto
		if db.query(models.Launches).filter(models.Launches.id == article['launches'][0]['id']).first() is not None:
			db_launches = db.query(models.Launches).filter(models.Launches.id == article['launches'][0]['id']).first()
			db_article.launches.append(db_launches)
		else:
			db_launches = models.Launches(id=article['launches'][0]['id'], provider=article['launches'][0]['provider'])
			db_article.launches.append(db_launches)

			#Adiciona no banco de dados
			db.add(db_launches)

	db.commit()
	return db_article

f = open("test.txt", "a")

def populate_database(db):
	for article in articles.json():
		f.write(str(article))

		#Cria um object com os dados recebidos do schema
		db_article = models.Articles(featured=article['featured'], title=article['title'], url=article['url'],
									imageUrl=article['imageUrl'], newsSite=article['newsSite'],
									summary=article['summary'], publishedAt=article['publishedAt'])

		#Adiciona no banco de dados
		db.add(db_article)
		db.commit()

		#Caso tenha events ou launches adiciona dentro do objeto artigo
		if article['events']:
			criar_event_launch("events", article, db_article, db)
		if article['launches']:
			criar_event_launch("launches", article, db_article, db)

		db.commit()

populate_database(db)
f.close()