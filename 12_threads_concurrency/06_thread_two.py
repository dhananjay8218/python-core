# thread_multiple_jobs — Running multiple jobs concurrently using threads

import threading
import time

def run_job(job_name, wait_time):
    # Performs a job that takes some time
    print(f"{job_name}: started...")
    time.sleep(wait_time)
    print(f"{job_name}: finished.")

t1 = threading.Thread(target=run_job, args=("Job A", 2))  #args as tuple
t2 = threading.Thread(target=run_job, args=("Job B", 3))

t1.start()
t2.start()
t1.join()
t2.join()

print("All jobs done.")
