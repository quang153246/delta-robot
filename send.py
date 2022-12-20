#!/usr/bin/env python
import pika
import cv2

camera = cv2.VideoCapture(0)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:

    try:
        ret, frame = camera.read()
        if ret:
            send_data = frame.tobytes()
            channel.basic_publish(exchange='', routing_key='hello', body=send_data)
    except KeyboardInterrupt:
        break

connection.close()