FROM mysql:latest
LABEL description="Custom MySQL image for an assignment, mainly including an init.sql file."
ENV MYSQL_ALLOW_EMPTY_PASSWORD=True
COPY init.sql /docker-entrypoint-initdb.d
EXPOSE 3306