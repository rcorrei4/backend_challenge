import requests

from schemas import schemas
from database.func import criar_event_launch
from database.settings import SessionLocal

# Dependency
db = SessionLocal()

print("Recebendo o número de artigos a serem adicionados...")
articles_count_request = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles/count")
articles_count = articles_count_request.json()

result = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles", params={"_limit": articles_count})
print(f"Adicionando {articles_count} artigos ao banco de dados...")

articles = result.json()

for article in list(reversed(articles)):
	article = schemas.Article.parse_obj(article)

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