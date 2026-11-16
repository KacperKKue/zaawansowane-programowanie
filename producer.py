
import os
import sys
import uuid
import time

QUEUE_FILE = "queue.txt"
LOCK_FILE = "queue.lock"


def acquire_lock():
    while True:
        try:
            return os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            time.sleep(0.1)


def release_lock(lock):
    os.close(lock)
    os.remove(LOCK_FILE)


def add_task():
    lock = acquire_lock()

    try:
        task_id = str(uuid.uuid4())

        with open(QUEUE_FILE, "a") as file:
            file.write(f"{task_id},pending\n")

        print(f"Dodano zadanie: {task_id}")

    finally:
        release_lock(lock)


count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for _ in range(count):
    add_task()
