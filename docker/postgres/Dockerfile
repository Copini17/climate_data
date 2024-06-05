FROM postgres:latest

WORKDIR /app

COPY ../docker/postgres/library/init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432