import threading
import time

def cpu_task():
    print(f"{threading.current_thread().name} started...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} ended...")


t1 = threading.Thread(target=cpu_task, name="Thread-1")
t2 = threading.Thread(target=cpu_task, name="Thread-2")

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"total time: {end - start:.2f} seconds")