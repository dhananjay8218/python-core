# thread_download — Concurrent downloads using threads
# Threads are ideal for I/O-bound tasks such as downloading files.

import threading
import requests
import time

def download_file(url):
    print(f"Starting download: {url}")
    response = requests.get(url)
    print(f"Completed download: {url} | Size: {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

# Create and start threads
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

end = time.time()
print(f"All downloads finished in {end - start:.2f} seconds")
