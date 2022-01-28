import requests

from src.database.crud import get_last_article, create_article
from src.database.settings import SessionLocal
from src.schemas import schemas

def check_articles():
	db = SessionLocal()

	print('Verificando o último artigo salvo...')
	last_article = get_last_article(db)

	print("Verificando se há novos artigos...")
	result = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles", params={"publishedAt_gt": last_article.publishedAt})
	articles = result.json()

	if articles:
		print(f"Adicionando {len(articles)} novos artigos ao banco de dados...")
		for article in list(reversed(articles)):
			article = schemas.Article.parse_obj(article)

			create_article(db, article)
			print("Artigos adicionados.")
	else:
		print("Não há novos artigos a serem adicionados.")