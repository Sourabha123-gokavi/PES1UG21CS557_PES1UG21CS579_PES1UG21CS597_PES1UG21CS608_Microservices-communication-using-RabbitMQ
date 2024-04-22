
import mysql.connector
import pika

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
queue_name = 'itemcreation'

# Declare the queue
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    conn = mysql.connector.connect(
        user="myuser",
        password="password",
        host="database",
        database="mydatabase",
    )
    curr=conn.cursor()

    msg=body.decode()
    data=msg.split(' ')
    print(f" [x] Received {data}")
    if(len(data)==2):
        curr.execute("select quantity from inventory where product_id=%s",(int(data[0]),))
        a=int(curr.fetchone()[0])
        curr.execute("update inventory set quantity=%s where product_id=%s",(a+int(data[1]),int(data[0]),))
    else:
        curr.execute("insert into inventory (product_name,quantity,unit_price,location) values (%s,%s,%s,%s)",(data[0],int(data[1]),float(data[2]),data[3]))

    conn.commit()

    curr.close()
    conn.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Subscribe to the queue and consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
