FROM python:3.9

ENV PYTHONBUFFERED 1

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install apt-utils gcc python3-dev

COPY ./requirements.txt /requirements
RUN pip install -r requirements

COPY ./.compose/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app
