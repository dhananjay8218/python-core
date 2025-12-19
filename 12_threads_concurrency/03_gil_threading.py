# gil_threading_example.py — CPU-heavy work using threading
# GIL (Global Interpreter Lock):
#   - Only one thread can execute Python bytecode at a time.
#   - Threads cannot run CPU-bound tasks in parallel.
#   - Good for I/O, slow for CPU work.
#
# Mutex (Mutual Exclusion):
#   - A lock used to protect shared data between threads.
#   - Prevents race conditions (only one thread accesses the resource at a time).
#
# Underscore (_) use:
#   - Throwaway variable in loops: for _ in range(10)
#   - Means “we don’t use this value”.

import threading
import time

def cpu_task():
    print(f"{threading.current_thread().name} started...")
    count = 0
    for _ in range(100_000_000):  # CPU-heavy loop
        count += 1
    print(f"{threading.current_thread().name} finished...")

t1 = threading.Thread(target=cpu_task, name="Thread-1")
t2 = threading.Thread(target=cpu_task, name="Thread-2")

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Threading total time (affected by GIL): {end - start:.2f} seconds")
