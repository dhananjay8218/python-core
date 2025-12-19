# threading_concurrency.py — Concurrency using threads
# Concurrency: multiple tasks making progress by sharing the same CPU.
# Threads are lightweight and best for I/O-bound work (waiting, printing, downloading, etc.).

import threading
import time

def handle_request():
    for i in range(1, 4):
        print(f"Handling request #{i}")
        time.sleep(1)  # simulates network I/O

def write_logs():
    for i in range(1, 4):
        print(f"Writing log entry #{i}")
        time.sleep(1.2)  # simulates disk I/O

# Creating threads for concurrent execution
request_thread = threading.Thread(target=handle_request)
log_thread = threading.Thread(target=write_logs)

request_thread.start()
log_thread.start()

# Wait for both to complete
request_thread.join()
log_thread.join()

print("All tasks completed (threading concurrency)")