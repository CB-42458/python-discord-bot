"""Program Used to Monitor and Restart bot.py"""
import subprocess
import time

import logger
import psutil

# Set maximum memory usage in bytes (50MB)
MAX_MEMORY = 50 * 1024 * 1024

# Set interval to check memory usage (10 minutes)
INTERVAL = 60 * 60

logger.log("INFO", "supervisor.py", "Starting bot.py")

# Continuously check the memory usage of the program
while True:
    # Start the program as a subprocess
    process = subprocess.Popen(['python3', 'bot.py'])
    while process.poll() is None:
        # check the memory usage of the subprocess
        memory_usage = psutil.Process(process.pid).memory_info().rss
        # convert the memory usage to MB to two decimal places
        memory_usage = round(memory_usage / 1024 / 1024, 2)

        logger.log("INFO", "supervisor.py", f"bot.py memory usage: {memory_usage} MB")

        if memory_usage > MAX_MEMORY:
            logger.log("INFO", "supervisor.py", "bot.py exceeded maximum memory usage, restarting...")
            process.terminate()
            break
        # Wait for the specified interval before checking memory usage again
        time.sleep(INTERVAL)

    logger.log("INFO", "supervisor.py", f"bot.py exited with code {process.returncode}")
    # print('supervisor.py | restarting bot.py in 5 seconds')
    logger.log("INFO", "supervisor.py", "restarting bot.py in 5 seconds")
    time.sleep(5)
