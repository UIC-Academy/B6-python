def log_parser(log_lines):
    """Generator that finds error messages in logs"""
    for line in log_lines:
        if "ERROR" in line:
            yield f"Found error: {line.strip()}"


# Simulated log data
logs = [
    "INFO: System started",
    "ERROR: Disk full",
    "INFO: User login",
    "ERROR: Connection timeout",
    "INFO: Backup completed",
]

# Process logs lazily - efficient for large files
for error in log_parser(logs):
    print(error)
