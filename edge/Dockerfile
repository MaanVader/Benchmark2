FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      openssh-client sshpass iputils-ping ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && (id www-data || useradd --create-home www-data) \
    && usermod --shell /bin/bash www-data

WORKDIR /srv/edge
COPY app.py .
COPY deploy.env /srv/edge/config/deploy.env
RUN chown -R www-data:www-data /srv/edge && chmod 640 /srv/edge/config/deploy.env
USER www-data
EXPOSE 8080
CMD ["python", "app.py"]
