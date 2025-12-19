# asyncio_with_threadpool.py — Running blocking code inside asyncio
# This pattern is used when you have:
# - an asyncio-based program
# - but also blocking (sync) functions that cannot be rewritten as async
#
# ThreadPoolExecutor allows blocking code to run without blocking the event loop.

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# Blocking function (normal synchronous code)
def check_inventory(item):
    print(f"Checking inventory for {item}...")
    time.sleep(3)  # blocking operation
    return f"{item} available: 42 units"


# Async entry point
async def main():
    loop = asyncio.get_running_loop()

    # Run blocking function in a separate thread
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(
            executor,
            check_inventory,
            "ItemA"
        )
        print(result)


# Start asyncio event loop
asyncio.run(main())
