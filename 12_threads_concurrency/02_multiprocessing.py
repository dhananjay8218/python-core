# multiprocessing_parallel.py — Parallel execution using processes
# Multiprocessing: runs tasks truly in parallel using multiple CPU cores.
# Useful for CPU-heavy tasks (calculations, image processing, ML tasks).

from multiprocessing import Process
import time

def compute_heavy_task(batch_id):
    print(f"Batch {batch_id} — start")
    total = 0
    for i in range(10_000_000):  # CPU-heavy loop
        total += i
    print(f"Batch {batch_id} — done (result: {total})")

if __name__ == "__main__":
    workers = [
        Process(target=compute_heavy_task, args=(i,))
        for i in range(1, 4)
    ]

    # Start parallel workers
    for w in workers:
        w.start()

    # Wait for all CPU tasks to finish
    for w in workers:
        w.join()

    print("All batches processed (multiprocessing parallelism)")
