FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements /app
COPY django_app /app 

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py runserver"]