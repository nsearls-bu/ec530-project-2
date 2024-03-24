from pika import BasicProperties
import pickle
from bridge import rabbitmq_client, redis_client
import time

def callback(ch, method, properties: BasicProperties, body):
    text_data = pickle.loads(body)
    time.sleep(5)
    result = "We've processed this data"
    print(f"Result: {result}")

    redis_client.set(properties.headers["task_id"], result)

    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbitmq_client.basic_qos(prefetch_count=1)
rabbitmq_client.basic_consume(queue='project2_queue', on_message_callback=callback)


if __name__ == '__main__':
    rabbitmq_client.start_consuming()
