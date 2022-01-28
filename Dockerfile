FROM python:3.9.7

COPY ./requirements.txt /home

WORKDIR /home

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=127.0.0.1", "--reload"]