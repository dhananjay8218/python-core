# Running CPU-heavy code inside asyncio
# This pattern is used when:
# - you have an asyncio-based application
# - and a CPU-heavy function that should not run in the event loop
#
# ProcessPoolExecutor runs the task in a separate process,
# bypassing the GIL and allowing true parallel execution.

import asyncio
from concurrent.futures import ProcessPoolExecutor


# CPU-heavy or CPU-sensitive function
def encrypt_data(text):
    # Simulates CPU work (simple transformation)
    return text[::-1]


# Async entry point
async def main():
    loop = asyncio.get_running_loop()

    # Run CPU-heavy task in a separate process
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(
            executor,
            encrypt_data,
            "account_number_1234"
        )
        print("Encrypted result:", result)


# Required entry point for multiprocessing on some platforms
if __name__ == "__main__":
    asyncio.run(main())
