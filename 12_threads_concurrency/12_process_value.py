from multiprocessing import Process, Value

def increment(counter):
    # Each process increments the shared counter many times
    for _ in range(100000):
        # Lock ensures only one process updates at a time
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    # Shared integer value ('i' = int), starting at 0
    counter = Value('i', 0)

    # Create 4 processes that will all update the same counter
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Print the final result after all increments
    print("Final counter value:", counter.value)
