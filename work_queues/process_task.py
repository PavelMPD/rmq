#!/usr/bin/env python
import time

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


queue_name = 'task_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue_name, durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    callback, queue=queue_name, no_ack=False)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
