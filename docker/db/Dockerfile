FROM mysql:5.7

#ADD ./mysql-init-files /docker-entrypoint-initdb.d
ENV MYSQL_DATABASE=schema
ENV MYSQL_ROOT_PASSWORD=db_password
EXPOSE 3306
CMD ["mysqld"]