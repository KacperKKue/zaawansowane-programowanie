
import os
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


def get_task():
    lock = acquire_lock()

    try:
        if not os.path.exists(QUEUE_FILE):
            return None

        with open(QUEUE_FILE, "r") as file:
            tasks = [line.strip().split(",") for line in file if line.strip()]

        for task in tasks:
            if task[1] == "pending":
                task[1] = "in_progress"

                with open(QUEUE_FILE, "w") as file:
                    for item in tasks:
                        file.write(f"{item[0]},{item[1]}\n")

                return task[0]

        return None

    finally:
        release_lock(lock)


def finish_task(task_id):
    lock = acquire_lock()

    try:
        with open(QUEUE_FILE, "r") as file:
            tasks = [line.strip().split(",") for line in file if line.strip()]

        for task in tasks:
            if task[0] == task_id:
                task[1] = "done"

        with open(QUEUE_FILE, "w") as file:
            for task in tasks:
                file.write(f"{task[0]},{task[1]}\n")

    finally:
        release_lock(lock)


print("Consumer uruchomiony!")

while True:
    task_id = get_task()

    if task_id:
        print(f"Pobrano zadanie: {task_id}")
        print("Wykonywanie zadania...")

        time.sleep(30)

        finish_task(task_id)

        print(f"Zakończono zadanie: {task_id}")

    else:
        print("Brak zadań. Oczekiwanie...")

        time.sleep(5)
