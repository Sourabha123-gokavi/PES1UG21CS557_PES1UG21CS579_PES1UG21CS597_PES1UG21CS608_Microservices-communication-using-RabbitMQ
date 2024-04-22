FROM python


RUN mkdir -p /home

COPY . /home

RUN pip install --no-cache-dir pika

CMD ["python","/home/one.py"]