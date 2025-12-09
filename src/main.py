from pathlib import Path

from parser import parse_log_file
from analyzer import count_by_level, filter_by_level


def main() -> None:
    log_path = Path(__file__).parent.parent / "logs" / "sample.log"

    entries = parse_log_file(log_path)
    stats = count_by_level(entries)

    print("=== Log Summary ===")
    for level, count in stats.items():
        print(f"{level}: {count}")

    # Exemplo: mostrar apenas erros
    error_entries = filter_by_level(entries, "ERROR")
    if error_entries:
        print("\nErrors found:")
        for e in error_entries:
            print(f"- {e.timestamp} | {e.message}")


if __name__ == "__main__":
    main()
