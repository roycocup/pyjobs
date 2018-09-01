FROM python:3.5.6-alpine3.7

RUN apk update && \
    apk add \
    bash \
    vim

WORKDIR /

COPY entrypoint.sh entrypoint.sh
RUN chmod 0777 entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]