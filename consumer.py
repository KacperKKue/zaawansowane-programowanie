
import pika
import json
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials("guest", "guest"),
        heartbeat=60
    )
)

channel = connection.channel()

channel.queue_declare(
    queue="conversations",
    durable=True
)


channel.basic_qos(prefetch_count=1)


def process_task(ch, method, properties, body):
    task = json.loads(body)

    task_id = task["id"]


    task["status"] = "in_progress"

    print(f"\nPobrano zadanie: {task_id}")
    print("Status: in_progress")
    print("Symulowanie rozmowy przez 30 sekund...")


    time.sleep(30)


    task["status"] = "done"

    print(f"Zakończono zadanie: {task_id}")
    print("Status: done")


    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue="conversations",
    on_message_callback=process_task
)

print("Consumer uruchomiony!")
print("Oczekiwanie na zadania...")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nZatrzymywanie consumera...")
    channel.stop_consuming()
    connection.close()
