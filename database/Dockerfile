# Use an official MySQL runtime as the base image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=password

# Set environment variables for database name and user
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=password
ENV DB_HOST=database
# Expose the MySQL port
EXPOSE 3306

# Start MySQL service automatically when the container starts
CMD ["mysqld"]
