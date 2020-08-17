# pull official base image
FROM python:3.7.8-buster

# set work directory
WORKDIR /usr/src/medline

RUN apt-get update && \
    apt-get install -y build-essential python nginx

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt

#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "medline:medline"]