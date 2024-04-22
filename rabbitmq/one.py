import pika

# Connection parameters for RabbitMQ running inside Docker container
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = 'password'

# Establish connection to RabbitMQ
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Define the queue names for this producer
queue_names = ['queue1', 'queue2', 'queue3']

for queue_name in queue_names:
    # Declare a queue
    channel.queue_declare(queue=queue_name)

    # Publish a message to the queue
    channel.basic_publish(exchange='', routing_key=queue_name, body='Hello, RabbitMQ!')

    print(f" [x] Sent 'Hello, RabbitMQ!' to queue '{queue_name}'")

# Close the connection to RabbitMQ
connection.close()
