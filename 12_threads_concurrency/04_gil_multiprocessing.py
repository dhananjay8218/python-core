# multiprocessing_parallel_example.py — CPU-heavy work using multiprocessing
# Multiprocessing:
#   - Creates separate processes with separate Python interpreters.
#   - Bypasses the GIL.
#   - Ideal for CPU-heavy tasks (parallel execution).
#
# Note: Each process runs independently and performs real parallel work.

from multiprocessing import Process
import time

def cpu_task():
    print("Process started...")
    count = 0
    for _ in range(100_000_000):  # CPU-heavy loop
        count += 1
    print("Process finished.")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=cpu_task)
    p2 = Process(target=cpu_task)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Multiprocessing total time (true parallelism): {end - start:.2f} seconds")
