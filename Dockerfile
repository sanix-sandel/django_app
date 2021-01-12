FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app
COPY ./django_app /app 

RUN pip3 install -r requirements.txt

#EXPOSE 8000
#ENTRYPOINT [ "python3" ]
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]