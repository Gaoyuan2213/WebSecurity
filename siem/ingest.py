from pathlib import Path
import json

def read_events(path):
    p = Path(path)
    if not p.exists():
        return []
    events = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                events.append(json.loads(line))
            except Exception:
                pass
    return events
