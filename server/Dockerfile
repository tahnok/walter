FROM python:3.8-buster

RUN apt-get update && apt-get install -y firefox-esr

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "server:app", "--host", "0.0.0.0"]