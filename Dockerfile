FROM ubuntu:18.04

MAINTAINER Chris Herman "cjherman6@gmail.com"

RUN apt-get update -y && \
    apt-get install git && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip

COPY . /app

WORKDIR /app

RUN cd fastai && \
    git pull && \
    conda env update

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "application.py" ]
