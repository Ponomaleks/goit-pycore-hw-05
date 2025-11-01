import sys
from typing import Generator, TextIO
from colorama import Fore
from collections import Counter


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return list(read_logs(file))
    except FileNotFoundError:
        print(f"{Fore.RED}Log file not found.{Fore.RESET}")
        return []


def read_logs(file: TextIO) -> Generator[dict, None, None]:
    for line in file:
        yield parse_log_line(line.strip())


def parse_log_line(line: str) -> dict:
    dict_names = ["date", "time", "level", "message"]
    date, time, log_lvl, *msg = line.split()
    msg = " ".join(msg)

    parts = [date, time, log_lvl, msg]
    return dict(zip(dict_names, parts))


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    header_level = "Рівень логування "
    header_value = "Кількість"
    print(f"{header_level} | {header_value}")
    print("-" * (len(header_level) + 1) + "|" + "-" * (len(header_value) + 1))
    for level, count in counts.items():
        print(f"{level:<{len(header_level)}} | {count:<{len(header_value)}}")


def display_logs(logs: list):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    args = sys.argv
    try:
        log_file_path = args[1]
    except IndexError:
        print("Перевірте, чи вказано шлях до файлу логів.")
        sys.exit()

    logs = load_logs(log_file_path)

    if not logs:
        sys.exit()

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        filter_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, filter_level)

        if filtered_logs:
            print(f"\nДеталі логів для рівня {filter_level}:")
            display_logs(filtered_logs)
