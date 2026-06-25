from collections import defaultdict

def parse_logs():
    event_counts = defaultdict(int)

    with open("logs.txt", "r") as file:
        for line in file:
            parts = line.strip().split()

            event_type = parts[0]
            target = parts[2] if len(parts) > 2 else "UNKNOWN"
            timestamp = parts[1] if len(parts) > 1 else "UNKNOWN"

            event_counts[(event_type, target)] += 1

    return event_counts