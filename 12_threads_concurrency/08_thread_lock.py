# thread_safe_counter — Using Lock to avoid race conditions
# A lock ensures only one thread modifies shared data at a time.

import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        # Lock ensures safe update of shared variable
        with lock:
            counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(10)]

# Start all threads
for t in threads:
    t.start()

# Wait for all to complete
for t in threads:
    t.join()

print(f"Final counter value: {counter}")
