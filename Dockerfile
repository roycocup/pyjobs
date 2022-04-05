FROM alpine:3.15.4

RUN apk update && \
    apk add \
    bash \
    vim

RUN apk update && apk add \
    python \
    python3 \
    py2-pip \
    py3-pip 

RUN pip install --upgrade pip

RUN pip install \
    virtualenv


RUN pip install virtualenv
# RUN pip install tensorflow


WORKDIR /app
COPY . . 

WORKDIR /app/src
RUN pip install -r requirements.txt

WORKDIR /app
COPY entrypoint.sh entrypoint.sh
RUN chmod 0777 entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]