# Asynchronous programming with asyncio
# Async programming allows tasks to run cooperatively without blocking the event loop.
# Best for I/O-bound work like waiting, network calls, timers, and async APIs.

import asyncio
import aiohttp


# Basic async function
async def simple_task():
    print("Task started...")
    await asyncio.sleep(2)  # non-blocking sleep
    print("Task completed")

# asyncio.run(simple_task())


# Multiple async tasks running concurrently
async def process_job(name, delay):
    print(f"Job {name} started")
    await asyncio.sleep(delay)  # DO NOT use time.sleep() in async code
    print(f"Job {name} finished")


# Async HTTP request example
async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} | Status: {response.status}")


async def main():
    # Run a single async task
    await simple_task()

    print("\nRunning multiple async jobs...\n")

    # Run multiple async tasks concurrently
    await asyncio.gather(
        process_job("A", 3),
        process_job("B", 3),
        process_job("C", 3),
    )

    print("\nRunning async HTTP requests...\n")

    # Async network calls using aiohttp
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)


# Entry point for asyncio programs
asyncio.run(main())
