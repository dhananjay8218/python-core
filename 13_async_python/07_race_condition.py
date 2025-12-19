# race_condition_example — Race condition without a lock
# A race condition occurs when multiple threads modify shared data
# at the same time without synchronization.

import threading

counter = 0  # shared resource

def increment_counter():
    global counter
    for _ in range(100_000):
        counter += 1  # NOT thread-safe

# Create multiple threads
threads = [
    threading.Thread(target=increment_counter)
    for _ in range(2)
]

# Start threads
for t in threads:
    t.start()

# Wait for threads to finish
for t in threads:
    t.join()

print("Final counter value:", counter) # 200000
