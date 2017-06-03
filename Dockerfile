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
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG DJANGO_SETTINGS_MODULE="openduty.settings_docker"
ARG DJANGO_SECRET_KEY="The SECRET_KEY setting must not be empty (even for collectstatic task)"
RUN ./manage.py collectstatic --noinput
EXPOSE 8000
CMD ./manage.py runserver 0.0.0.0:8000
