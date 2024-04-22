import pika
import mysql.connector
# Connection parameters for RabbitMQ running inside Docker container
rabbitmq_host = 'rabbitmqcontainer'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = 'password'

# Establish connection to RabbitMQ
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Define the queue name for this consumer
queue_name = 'orderprocessing'


def callback(ch, method, properties, body):

    conn = mysql.connector.connect(
        user="myuser",
        password="password",
        host="database",
        database="mydatabase",
    )
    curr=conn.cursor()

    msg=body.decode();
    data=msg.split(' ')         #msg=orderid

    curr.execute('update orders set stats=%s where order_id=%s',('Delivered',int(data[0])))
    conn.commit()

    curr.close()
    conn.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

# Subscribe to the queue and consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
