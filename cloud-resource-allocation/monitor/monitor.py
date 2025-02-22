import time
import psutil
from datetime import datetime

def monitor_resources():
    with open("resource_log.txt", "a") as log_file:  # Open a log file in append mode
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_entry = f"{timestamp} | CPU: {cpu_usage}% | RAM: {memory_usage}%"
            print(log_entry)
            log_file.write(log_entry + "\n")  # Save to file

            time.sleep(5)  # Refresh every 5 seconds

print("Starting resource monitoring...")
monitor_resources()
