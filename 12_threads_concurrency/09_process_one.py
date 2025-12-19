import threading
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):   # CPU-heavy work
        total += i
    print("DONE ✅")

# Measure how long the whole threaded work takes
start = time.time()

# Create 2 threads to run the same CPU task
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Time taken: {time.time() - start:.2f} seconds")
