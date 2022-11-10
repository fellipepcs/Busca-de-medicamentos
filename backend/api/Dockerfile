FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=mysite.settings.prod" ]