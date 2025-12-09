![Python Version](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Type](https://img.shields.io/badge/Type-Automation-blueviolet)

# Log Monitoring & Automation System (Python)

A small but practical log monitoring tool designed to simulate part of a NOC (Network Operations Center) workflow.  
The project reads log files, parses structured entries, analyzes error levels, generates reports, and raises basic alerts — making it useful for IT Support, NOC operations and automation practices.

---

## 🔧 Features

- Parse log files into structured Python objects using `regex` and `dataclasses`
- Count log entries by severity level (`INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- Filter entries by level
- Generate automated reports:
  - JSON report (`reports/log_report_YYYYMMDD_HHMMSS.json`)
  - Text summary (`reports/log_summary_YYYYMMDD_HHMMSS.txt`)
- Simple alert rule for detected anomalies (e.g., multiple errors or any critical events)
- Modular architecture for scalability

---

## 📂 Project Structure

```
log-monitor-automation/
├── logs/
│   └── sample.log
├── reports/
├── src/
│   ├── parser.py
│   ├── analyzer.py
│   ├── reporter.py
│   └── main.py
└── README.md
```

- `parser.py` → Extracts timestamp, level and message from log lines  
- `analyzer.py` → Counts and filters logs  
- `reporter.py` → Exports text and JSON reports  
- `main.py` → Orchestrates the full workflow  

---

## 🧠 How It Works

1. You place a `.log` file inside the `logs/` folder  
2. Run the project:  
   ```bash
   python -m src.main
   ```
3. The tool:
   - Reads and parses each log entry
   - Aggregates severity stats
   - Prints a summary in the terminal
   - Detects anomalies and raises an alert
   - Generates reports automatically

---

## 📊 Example Output

```
=== Log Summary ===
INFO: 3
WARNING: 1
ERROR: 1
CRITICAL: 1

Errors found:
- 2025-01-01 10:02:35 | Failed to connect to database

[ALERT] High number of errors/critical events detected.

JSON report saved at: reports/log_report_20250101_120000.json
Text summary saved at: reports/log_summary_20250101_120000.txt
```

---

## 💡 Why This Project Matters

This project demonstrates real-world skills used in IT Support, NOC operations and automation roles:

- Log parsing  
- Error analysis  
- Monitoring logic  
- Python scripting  
- Modular architecture  
- Basic alerting  
- Report generation  

It reflects tasks performed daily in environments involving system stability, incident response and operational monitoring.

---

## 🚀 Future Improvements (Roadmap)

- Email or Slack alert integration  
- Support for multiple log files at once  
- Dashboard visualization  
- Docker containerization  
- Real-time log streaming with watchers  

---

## 🧑‍💻 Technologies Used

- Python 3  
- Regex for pattern matching  
- Dataclasses for structured modeling  
- JSON for report exporting  
- Pathlib for filesystem operations  

---

## 📬 Contact

Feel free to connect with me on LinkedIn:

**linkedin.com/in/ethical-leonardo**
