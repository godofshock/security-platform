import datetime

def log_event(event):
    with open("reports/log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {event}\n")
