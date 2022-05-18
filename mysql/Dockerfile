FROM mysql:latest
COPY init.sql /docker-entrypoint-initdb.d
LABEL description="Custom MySQL image for an assignment, mainly including an init.sql file."
EXPOSE 3306