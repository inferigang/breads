FROM python:3.10
LABEL maintainer="oppsec <https://github.com/oppsec>"

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PIP_NO_CACHE_DIR=off

WORKDIR /breads

RUN apt-get update && \
    apt-get install -y openssl python3 git apt-utils pipx

# Create directories
COPY . .

# Install libraries and run
RUN pipx ensurepath
RUN pipx install git+https://github.com/inferigang/breads --include-deps
CMD ["breads-ad"]