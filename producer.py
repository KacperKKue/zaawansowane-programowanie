
import pika
import uuid
import json
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials("guest", "guest")
    )
)


channel = connection.channel()

channel.queue_declare(
    queue="conversations",
    durable=True
)


count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for i in range(count):
    task = {
        "id": str(uuid.uuid4()),
        "status": "pending"
    }

    channel.basic_publish(
        exchange="",
        routing_key="conversations",
        body=json.dumps(task),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print(f"Dodano zadanie: {task['id']}")

connection.close()
