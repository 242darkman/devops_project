FROM mysql:8.2.0

ENV MYSQL_ROOT_PASSWORD=MYSQL_ROOT_PASSWORD
ENV MYSQL_DATABASE=iterator-db

COPY 1-SCHEMA.sql /docker-entrypoint-initdb.d/
COPY 2-PRIVILEGES.sql /docker-entrypoint-initdb.d/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mysqld"]