import pika

# Connection parameters for RabbitMQ running inside Docker container
rabbitmq_host = 'rabbitmqcontainer'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = 'password'

try:
    # Establish connection to RabbitMQ
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    print("Connected to RabbitMQ")

    # Define the queue names for this producer
    queue_names = ['healthcheck', 'stockmanagement', 'orderprocessing', 'itemcreation']

    for queue_name in queue_names:
        # Declare a queue
        channel.queue_declare(queue=queue_name)

    def Itemcreation(msg):
        
        channel.basic_publish(exchange='',routing_key='itemcreation',body=msg)
        print("sucessfully sent")

    def Stockmanagement():
        msg='productname 10 1'
        channel.basic_publish(exchange='',routing_key='stockmanagement',body=msg)
        print("sucessfully sent")

    def Orderprocessing():
        msg='1'
        channel.basic_publish(exchange='',routing_key='orderprocessing',body=msg)
        print("sucessfully sent")

    msg="productname 10 1.2 mumbai"
    Itemcreation(msg)
    msg="1 10"
    Itemcreation(msg)
    Stockmanagement()
    Orderprocessing()
    

except pika.exceptions.AMQPConnectionError as e:
    print("Failed to connect to RabbitMQ:", repr(e))




