# pull official base image
FROM python:3.9.6-alpine

# set work directory
RUN pip install pipenv
WORKDIR /usr/src/cars/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . /usr/src/cars/
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
