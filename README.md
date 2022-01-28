# Back-end Challenge 2021 🏅 - Space Flight News


## Sobre o projeto
RESTful API inspirada na Space Flight News API, que faz possível criar, editar, atualizar e excluir artigos que foram extraídos da Space Flight News API.

### Ferramentas

- Python 3.9.7
- FastAPI
- PostgreSQL

## Instalação utilizando docker
Siga os passos a seguir para rodar o projeto

Clone este repositório no seu dispositivo
~~~shell
git clone https://github.com/rcorrei4/backend_challenge.git
~~~

Após isso
~~~shell
cd backend_challenge
~~~

Criar imagem do docker
~~~shell
docker build -t backend_challenge .
~~~

## Rodar o projeto

Antes de tudo renomeie o arquivo `.env.example` para `.env` e insira a url do banco de dados na variável `SQLALCHEMY_DATABASE_URL`

Após isso execute o script para preencher o banco de dados:
~~~shell
python3 src/populate_database.py
~~~


> This is a challenge by Coodesh