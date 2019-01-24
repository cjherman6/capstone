FROM ubuntu:18.04

MAINTAINER Chris Herman "cjherman6@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip

COPY . /app

WORKDIR /app

RUN ssh -i fastaiCapstone.pem ubuntu@52.2.104.31 -L8888:localhost:8888 && \
    cd fastai && \
    git pull && \
    conda env update

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "application.py" ]
