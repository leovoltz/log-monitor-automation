from pathlib import Path
from typing import Dict
import json
from datetime import datetime

def save_json_report(stats: Dict[str, int], output_dir: Path) -> Path:
    """
    Saves a JSON report containing the log counts by severity level.
    Example: {"INFO": 10, "WARNING": 2, "ERROR": 3}
    """    
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"log_repott_{timestamp}.json"

    with report_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "generated_at": datetime.now().isoformat(),
                "stats_by_level": stats,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    return report_path

def save_text_summary(stats: Dict[str, int], output_dir: Path) -> Path:
    """
    Saves a simple, human-readable text summary of the log statistics.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"log_summary{timestamp}.txt"

    lines = [
        f"Log Summary - generated at {datetime.now().isoformat()}",
        "",
    ]
    for level, count in stats.items():
        lines.append(f"{level}: {count}")

    report_path.write_text("\n".join(lines), encoding="utf-8")

    return report_path