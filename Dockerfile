FROM python:2

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      libldap2-dev \
      libsasl2-dev \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
