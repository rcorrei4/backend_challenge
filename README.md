# Back-end Challenge 2021 🏅 - Space Flight News

## Sobre o projeto
RESTful API inspirada na Space Flight News API, que faz possível criar, editar, atualizar e excluir artigos que foram extraídos da Space Flight News API.

### Ferramentas

- Python 3.9.7
- FastAPI
- PostgreSQL

## Instalação utilizando docker
Siga os passos a seguir para instalar o projeto `(Necessário ter o Python 3.9 ou acima instalado!)`

<br />

Clone este repositório no seu dispositivo:
~~~shell
git clone https://github.com/rcorrei4/backend_challenge.git
~~~

Após isso:
~~~shell
cd backend_challenge
~~~

Crie a imagem do docker:
~~~shell
docker build -t backend_challenge .
~~~
<br />

## Rodar o projeto

Antes de tudo renomeie o arquivo `.env.example` para `.env` e insira a url do banco de dados na variável `SQLALCHEMY_DATABASE_URL`

Após isso execute o script para preencher o banco de dados:
~~~shell
python3 src/populate_database.py
~~~

E finalmente inicie o app:
~~~shell
sudo docker run --env-file .env -p 8000:8000 -t -i backend_challenge
~~~
<br />

Para acessar o app digite o seguinte link no navegador:
`127.0.0.1:8000`
<br />

> This is a challenge by [Coodesh](https://coodesh.com/)

<br />
[Apresentação](https://www.loom.com/embed/00724eac18db4acc892372ab248c0889)