from datetime import datetime
from pathlib import Path


def analyze_heartbeat_log(input_file="hblog.txt", output_file="hb_test.log"):
    key_filter = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    # Читаємо лог-файл
    with open(input_file, "r") as file:
        for line in file:
            if key_filter in line:
                ts_index = line.find("Timestamp ")
                if ts_index != -1:
                    time_str = line[ts_index + 10 : ts_index + 18]  # Витягуємо HH:MM:SS
                    try:
                        timestamps.append(
                            (datetime.strptime(time_str, "%H:%M:%S"), line.strip())
                        )
                    except ValueError:
                        continue  # Пропускаємо некоректні рядки

    # Аналізуємо пари часових відміток
    with open(output_file, "w") as log_file:
        for i in range(len(timestamps) - 1):
            current_time, current_line = timestamps[i]
            next_time, next_line = timestamps[i + 1]

            delta = abs((next_time - current_time).total_seconds())

            if 31 < delta < 33:
                log_file.write(
                    f"WARNING at {next_time.time()} — Heartbeat gap: {delta:.1f}s\n"
                )
            elif delta >= 33:
                log_file.write(
                    f"ERROR at {next_time.time()} — Heartbeat gap: {delta:.1f}s\n"
                )

    print(f"Готово. Результат записано у файл: {output_file}")

if __name__ == "__main__":
    analyze_heartbeat_log()