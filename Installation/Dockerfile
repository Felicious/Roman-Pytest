FROM jenkinsci/jenkins:2.134-alpine

USER root

RUN apk add --no-cache \
			python\
			python-dev \
            ca-certificates \
            curl \
            openssl \
            py-pip \
			build-base \
    && rm -rf /var/cache/apk/*

RUN pip install pytest

# Installing Docker and Compose...
# See https://hub.docker.com/_/docker/ for updates.
ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.12.3
ENV DOCKER_SHA256 626601deb41d9706ac98da23f673af6c0d4631c4d194a677a9a1a07d7219fa0f
RUN set -x \
    && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
    && echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
    && tar -xzvf docker.tgz \
    && mv docker/* /usr/local/bin/ \
    && rmdir docker \
    && rm docker.tgz \
    && docker -v
RUN pip install docker-compose
