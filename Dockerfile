FROM python:latest

COPY . /app

WORKDIR /app

RUN apt-get update && apt -y upgrade

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]