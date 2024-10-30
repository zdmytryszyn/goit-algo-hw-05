import sys
from pathlib import Path
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    split_line = line.strip().split(" ", 3)
    return {
        "date": split_line[0],
        "time": split_line[1],
        "level": split_line[2],
        "message": split_line[3]
    }


def load_logs(file_path: str) -> list:
    path = Path(file_path)
    logs = []
    if path.exists():
        with open(f"{path}", "r", encoding="utf-8") as logfile:
            for log in logfile.readlines():
                logs.append(parse_log_line(log))
        return logs
    else:
        print(
            f"Path \"{path.absolute()}\" does not exist, check!"
        )


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: dict) -> None:
    len_left = len("Рівень логування ")
    len_right = len(" Кількість")
    print(
        "Рівень логування | Кількість",
        "-" * len_left + "|" + "-" * len_right,
        sep="\n"
    )
    for count in counts:
        print(f"{count:^{len_left}}|{counts[count]:^{len_right}}")


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = ""

    if file_path:
        logs = load_logs(file_path)
        count_by_level = count_logs_by_level(logs)
        display_log_counts(count_by_level)

        try:
            cmd = Path(sys.argv[2])
        except IndexError:
            cmd = ""

        if cmd:
            filtered_logs = filter_logs_by_level(logs, str(cmd))
            print(f"Деталі логів для рівня '{str(cmd).upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print("No file path given")
