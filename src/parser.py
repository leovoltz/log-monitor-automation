from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
import re
from typing import List


@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str

# Regex to match log lines in the format:
LOG_LINE_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>[A-Z]+)\] (?P<message>.*)$"
)


def parse_log_file(path: Path) -> List[LogEntry]:
    entries: List[LogEntry] = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  #skip empty lines


            match = LOG_LINE_PATTERN.match(line)
            if not match:
                # optional: log or collect invalid lines for debugging
                continue

            ts_str = match.group("timestamp")
            level = match.group("level")
            message = match.group("message")

            timestamp = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")

            entries.append(LogEntry(timestamp=timestamp, level=level, message=message))

        return entries
