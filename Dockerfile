FROM ubuntu:20.04

RUN mkdir /app
ADD ./spaceproj /app
ADD requirements.txt /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

RUN apt-get update && apt-get install -y gnupg2 wget

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list


ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y gcc python3-dev musl-dev curl postgresql-14  python3-pip

RUN alias python=python3.8


RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY ./spaceproj .