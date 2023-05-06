import datetime as dt
import subprocess
import time
import psutil

# Set maximum memory usage in bytes (50MB)
MAX_MEMORY = 50 * 1024 * 1024

# Set interval to check memory usage (10 minutes)
INTERVAL = 60 * 10

print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
      f'\033[0;35msupervisor.py \033[0;31m Starting bot.py\033[0;0m', flush=True)

# Continuously check the memory usage of the program
while True:
    # Start the program as a subprocess
    process = subprocess.Popen(['python3', 'bot.py'])
    while process.poll() is None:
        # check the memory usage of the subprocess
        memory_usage = psutil.Process(process.pid).memory_info().rss
        # convert the memory usage to MB to two decimal places
        memory_usage = round(memory_usage / 1024 / 1024, 2)

        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35msupervisor.py\033[0;31m bot.py memory usage: {memory_usage} MB\033[0;0m', flush=True)

        if memory_usage > MAX_MEMORY:
            # print('supervisor.py | bot.py exceeded maximum memory usage, restarting...')
            print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
                  f'\033[0;35msupervisor.py\033[0;31m boy.py exceeded maximum memory usage, restarting...\033[0;0m',
                  flush=True)
            process.terminate()
            break
        # Wait for the specified interval before checking memory usage again
        time.sleep(INTERVAL)
    
    # print('supervisor.py | bot.py exited with code', process.returncode)
    print('\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
          f'\033[0;35msupervisor.py\033[0;31m bot.py exited with code {process.returncode}\033[0;0m', flush=True)
    print('\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
          f'\033[0;35msupervisor.py\033[0;31m restarting bot.py in 5 seconds\033[0;0m', flush=True)
    time.sleep(5)
           