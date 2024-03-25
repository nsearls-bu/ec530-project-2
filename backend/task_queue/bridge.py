import pika
from pika import PlainCredentials
import redis

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="rabbitmq",
        port=5672,
    )
) 
# Set up connection to RabbitMQ
rabbitmq_client = connection.channel()
rabbitmq_client.queue_declare(queue="project2_queue")

redis_client = redis.Redis(host="redis", port=6379)
