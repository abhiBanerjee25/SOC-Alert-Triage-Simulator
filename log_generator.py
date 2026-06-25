import random

events = ["FAILED_LOGIN", "PORT_SCAN", "MALWARE_DETECTED"]
targets = ["server1", "db01", "laptop7", "web01"]

with open("logs.txt", "w") as f:
    for _ in range(30):
        f.write(f"{random.choice(events)} {random.randint(1,5)} {random.choice(targets)}\n")