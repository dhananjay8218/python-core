# non_daemon_thread_example.py — Non-daemon thread example
# A non-daemon thread keeps the program alive until it finishes.
# If the thread runs an infinite loop, the program will not exit.

import threading
import time


def background_monitor():
    while True:
        print("Monitoring system status...")
        time.sleep(2)


# Create a non-daemon thread (default behavior)
monitor_thread = threading.Thread(
    target=background_monitor
)

monitor_thread.start()

print("Main program finished (but program will keep running)")
