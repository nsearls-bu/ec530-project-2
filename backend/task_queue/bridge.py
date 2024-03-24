import pika
from pika import PlainCredentials
import redis

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5673,
    )
) 
# Set up connection to RabbitMQ
rabbitmq_client = connection.channel()
rabbitmq_client.queue_declare(queue="project2_queue")

redis_client = redis.Redis(host="localhost", port=6378)
