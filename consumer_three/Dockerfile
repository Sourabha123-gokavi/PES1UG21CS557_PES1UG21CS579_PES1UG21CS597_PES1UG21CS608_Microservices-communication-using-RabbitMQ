FROM python

RUN mkdir -p /home

copy . /home

RUN pip install --no-cache-dir pika mysql-connector-python


CMD ["python","/home/one.py"]