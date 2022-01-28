import requests

from core.schemas import schemas
from core.database.crud import create_article
from core.database.settings import SessionLocal

# Dependency
db = SessionLocal()

print("Contando o número de artigos a serem adicionados...")
articles_count_request = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles/count")
articles_count = articles_count_request.json()

result = requests.get(url="https://api.spaceflightnewsapi.net/v3/articles", params={"_limit": articles_count, "_start": 1})
print(f"Adicionando {articles_count} artigos ao banco de dados...")

articles = result.json()

for article in list(reversed(articles)):
	article = schemas.Article.parse_obj(article)

	create_article(db, article)