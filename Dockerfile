FROM python:3.9.7

WORKDIR /home

COPY ./requirements.txt /home

RUN pip3 install -r requirements.txt


COPY ./src /home/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]