# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /031_test_Fevernova_BMAT_Spain

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
ADD requirements.txt /031_test_Fevernova_BMAT_Spain/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project
COPY  . /031_test_Fevernova_BMAT_Spain/

# run entrypoint.sh
ENTRYPOINT ["/031_test_Fevernova_BMAT_Spain/entrypoint.sh"]
