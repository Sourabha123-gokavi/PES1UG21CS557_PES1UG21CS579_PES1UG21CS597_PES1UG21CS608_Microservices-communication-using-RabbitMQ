# Use Python base image
# this includes the python pre installed and it serves as the foundation for the container
FROM python

# Set the working directory in the container
#all the subsequent commands are inthe docker file will be executed to this directory.
# if the directory doesn't exist docker will create it
WORKDIR /home

# Copy the application files to the container
# this will copy all the files which are present in the currenty directory to the home directory
COPY . /home

# Install dependencies
#this will all the dependency 
# pika for library for interacting with rabbitmq
# flask for web applicatoin framawork
# no cache to ensures the no acahe used during the installation 
# reducing the docker image file size by not keeping the unecessary files after installation

RUN pip install --no-cache-dir pika Flask mysql-connector-python

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
