from multiprocessing import Process, Queue


def worker_task(queue):
    # Send a message/result to the main process
    queue.put("Task completed")


if __name__ == "__main__":
    # Queue for communication between processes
    queue = Queue()

    # Create a worker process and pass the queue to it
    p = Process(target=worker_task, args=(queue,))

    p.start()  # Start worker
    p.join()  # Wait for worker to finish

    # Receive the result message
    print(queue.get())
