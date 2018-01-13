import sys
import pika


message = ' '.join(sys.argv[1:]) or "Create a task."

queue_name = 'task_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue_name, durable=True)
channel.basic_publish(
    exchange='', routing_key=queue_name, body=message,
    properties=pika.BasicProperties(delivery_mode=2)) # make message persistent
print(" [x] Sent '{}'".format(message))
connection.close()
