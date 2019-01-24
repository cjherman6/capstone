FROM ubuntu:18.04

MAINTAINER Chris Herman "cjherman6@gmail.com"

RUN apt-get update -y

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]
