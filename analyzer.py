from pathlib import Path
from collections import defaultdict

LOG_FILE = Path(__file__).resolve().parent / "logs.txt"

def parse_logs():
    event_counts = defaultdict(int)

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()

            if not parts:
                continue

            event_type = parts[0]
            target = parts[2] if len(parts) > 2 else "UNKNOWN"

            event_counts[(event_type, target)] += 1

    return event_counts