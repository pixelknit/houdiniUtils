import os
import psutil
import time

MEMORY_LIMIT_GB = 10

while True:
    for process in psutil.process_iter(["pid","name","memory_info"]):
        if process.info["name"] == "happrentice":
            memory_usage_gb = process.info["memory_info"].rss / 1024**3
            print(f"Houdini Memory Usage: {memory_usage_gb:.2f} GB")

            if memory_usage_gb > MEMORY_LIMIT_GB:
                try:
                    process.kill()
                    print("Houdini has been killed due to high memory usage")
                except psutil.NoSuchProcess:
                    print("Process no longer exists")


    time.sleep(2)
