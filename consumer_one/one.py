import mysql.connector
import pika
import time

rabbitmq_host = 'rabbitmqcontainer'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = 'password'

# Establish connection to RabbitMQ
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue_name='healthcheck'
def send_health_check(consumer_name):
    try:
        channel.basic_publish(exchange='', routing_key=consumer_name, body='Health Check')
        print(f"Health check message sent to consumer: {consumer_name}")
    except Exception as e:
        print("Failed to send health check:", e)

def health_check_callback(ch, method, properties, body):
    consumer_name = method.routing_key
    
    print(f"Received health check from consumer: {consumer_name}")



def send_health_check():
    consumers=['healthcheck', 'stockmanagement', 'orderprocessing', 'itemcreation']
    for consumer in consumers:
        send_health_check(consumer)

channel.basic_consume(queue=queue_name, on_message_callback=send_health_check, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

