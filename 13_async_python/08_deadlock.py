# deadlock_example.py — Deadlock in threading
# Deadlock occurs when two or more threads wait forever for each other
# to release resources (locks).

import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task_one():
    with lock_a:
        print("Task 1 acquired lock A")
        time.sleep(1)  # forces context switch
        with lock_b:
            print("Task 1 acquired lock B")


def task_two():
    with lock_b:
        print("Task 2 acquired lock B")
        time.sleep(1)  # forces context switch
        with lock_a:
            print("Task 2 acquired lock A")


t1 = threading.Thread(target=task_one)
t2 = threading.Thread(target=task_two)

t1.start()
t2.start()

t1.join()
t2.join()

print("This line will never be reached due to deadlock")
