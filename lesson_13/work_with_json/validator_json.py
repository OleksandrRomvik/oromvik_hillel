import os
import json
import logging

# Налаштування логера
logging.basicConfig(
    filename="json__Romanchenko.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

# Формуємо абсолютний шлях
folder_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".",  # поточна папка
    )
)
print("Список файлів у папці:")
print(os.listdir(folder_path))

# перевірка кожного json
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        filepath = os.path.join(folder_path, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                json.load(f)
            logging.info(f"{filename} — валідний JSON")
        except json.JSONDecodeError as e:
            logging.error(f"{filename} — невалідний JSON: {e}")
        except Exception as e:
            logging.error(f"{filename} — помилка при читанні: {e}")

print("Перевірка завершена. Результати у json__Romanchenko.log")
logging.shutdown()
