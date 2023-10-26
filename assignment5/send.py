import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='cs361')

channel.basic_publish(exchange='', routing_key='cs361', body='A message from CS361')
print(" [x] Sent 'A message from CS361'")
connection.close()