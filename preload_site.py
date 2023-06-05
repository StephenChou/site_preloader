#!/usr/bin/python3

# Script to easily preload site to avoid long loading.
# Cron expression for every 15 minutes: */15 * * * * 

import requests
import time
from datetime import datetime

# Current time and date for logging purposes
cur_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# read urls file
urls = []
with open("urls.txt", "r") as urls_file:
    urls = urls_file.read().splitlines()

urls_file.close()

# open log file
log_file = open("log.txt", "a")

# send a request for each url specified
for url in urls:
    start = time.time()

    r = requests.get(url)

    log = f"[{cur_datetime}] - "

    if r.status_code != 200:
        log += f"ERROR: Site \"{url}\" could not be reached (HTTP: {r.status_code})"
    else:
        log += f"SUCCESS: Site \"{url}\" was loaded."
    
    end = time.time()

    elapsed = end - start

    log += f" ({elapsed} seconds)\n"

    print(log)
    log_file.write(log)

log_file.close()
