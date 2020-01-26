FROM ubuntu:18.04

ENV DEBIAN_FRONTEND "noninteractive"

ENV VER "2.12.2"

RUN mkdir /usr/src/nzbhydra2 /data
WORKDIR /usr/src/nzbhydra

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip \
    openjdk-11-jdk-headless python3 wget python3-requests \
    python3-yaml

RUN wget -q https://github.com/theotherp/nzbhydra2/releases/download/v${VER}/nzbhydra2-${VER}-linux.zip && \
    unzip nzbhydra2-${VER}-linux.zip &&  \
    chmod 755 nzbhydra2

RUN useradd nzbhydra && \
    chown nzbhydra /data

USER nzbhydra
WORKDIR /usr/src/nzbhydra

COPY configure-nzbhydra.py ./
COPY entrypoint.sh ./

CMD ./entrypoint.sh
