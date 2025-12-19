# daemon_thread_example.py — Daemon thread example
# A daemon thread runs in the background and stops automatically
# when the main program exits.

import threading
import time


def background_monitor():
    while True:
        print("Monitoring system status...")
        time.sleep(2)


# Create a daemon thread
monitor_thread = threading.Thread(
    target=background_monitor,
    daemon=True
)

monitor_thread.start()

print("Main program finished")
