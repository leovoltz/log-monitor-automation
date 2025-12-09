from pathlib import Path

from .parser import parse_log_file
from .analyzer import count_by_level, filter_by_level
from .reporter import save_json_report, save_text_summary


def main() -> None:
    base_dir = Path(__file__).parent.parent  # pasta raiz do projeto
    log_path = base_dir / "logs" / "sample.log"
    output_dir = base_dir / "reports"

    if not log_path.exists():
        print(f"[ERROR] Log file not found: {log_path}")
        return

    entries = parse_log_file(log_path)
    if not entries:
        print("[WARNING] No valid log entries found.")
        return

    stats = count_by_level(entries)

    print("=== Log Summary ===")
    for level, count in stats.items():
        print(f"{level}: {count}")

    # Mostrar erros
    error_entries = filter_by_level(entries, "ERROR")
    critical_entries = filter_by_level(entries, "CRITICAL")

    if error_entries:
        print("\nErrors found:")
        for e in error_entries:
            print(f"- {e.timestamp} | {e.message}")

    # Regra simples de alerta: se tiver CRITICAL ou muitos ERRORs
    if len(critical_entries) > 0 or len(error_entries) >= 3:
        print("\n[ALERT] High number of errors/critical events detected.")

    # Gerar relatórios
    json_report_path = save_json_report(stats, output_dir)
    text_report_path = save_text_summary(stats, output_dir)

    print(f"\nJSON report saved at: {json_report_path}")
    print(f"Text summary saved at: {text_report_path}")


if __name__ == "__main__":
    main()
