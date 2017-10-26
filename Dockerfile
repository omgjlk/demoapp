FROM python:alpine

RUN apk --no-cache add --update \
    git

RUN git clone https://github.com/j2sol/demoapp.git /demoapp
RUN pip install -e /demoapp
RUN pip install rpdb

RUN apk del git

CMD demoapp
