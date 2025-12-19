# thread_tasks — Running two independent tasks concurrently using threads

import threading
import time

def heat_water():
    # Simulates warming up water (I/O-like wait)
    print("Heating water...")
    time.sleep(2)
    print("Water heated.")

def load_data():
    # Simulates reading or loading a resource
    print("Loading data...")
    time.sleep(3)
    print("Data loaded.")

start = time.time()

t1 = threading.Thread(target=heat_water)
t2 = threading.Thread(target=load_data)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()
print(f"Tasks completed in {end - start:.2f} seconds")
