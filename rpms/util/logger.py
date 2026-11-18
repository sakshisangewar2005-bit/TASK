from datetime import datetime

def log_activity(message):
    with open("activity_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {message}\\n")
