from collections import Counter
from typing import List, Dict

from .parser import LogEntry


def count_by_level(entries: List[LogEntry]) -> Dict[str, int]:
    counter = Counter(entry.level for entry in entries)
    return dict(counter)


def filter_by_level(entries: List[LogEntry], level: str) -> List[LogEntry]:
    level = level.upper()
    return [entry for entry in entries if entry.level == level]
