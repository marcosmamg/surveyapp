FROM python:3.6.8-alpine3.9
ENV PYTHONUNBUFFERED 1
RUN apk update
RUN apk add --no-cache python3-dev mariadb-dev gcc libc-dev unixodbc-dev
RUN mkdir /surveyapp
WORKDIR /surveyapp
COPY requirements.txt /surveyapp/
RUN pip install -r requirements.txt
COPY . /surveyapp/