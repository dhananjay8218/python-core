# asyncio_with_background_thread.py — Using asyncio with a background thread
# This example shows:
# - asyncio running the main async task
# - a daemon thread running in the background
# - both working together without blocking each other

import asyncio
import threading
import time


# Background task running in a separate thread
def background_logger():
    while True:
        time.sleep(1)  # blocking sleep is fine inside a thread
        print("Background: system health check")


# Async task managed by asyncio event loop
async def fetch_data():
    await asyncio.sleep(3)  # non-blocking async sleep
    print("Async task: data fetched")


# Start background thread (daemon=True means it stops with main program)
threading.Thread(
    target=background_logger,
    daemon=True
).start()


# Run asyncio task
asyncio.run(fetch_data())
