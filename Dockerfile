# pull official base image
FROM python:3.9.18-slim-bullseye

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME /app

# set work directory
WORKDIR ${APP_HOME}

RUN addgroup --system django \
  && adduser --system --ingroup django django

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# install dependencies
ADD ./requirements.txt /requirements.txt
RUN pip3 install -U pip
RUN pip3 install -r /requirements.txt

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# copy project
COPY . .

RUN chown django:django ${APP_HOME}
USER django

# run entrypoint
ENTRYPOINT ["/entrypoint"]
