import logging
import xml.etree.ElementTree as ET

# Налаштування логера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_incoming_value(xml_file_path, target_number):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for group in root.findall(".//group"):
            number_elem = group.find("./number")
            if number_elem is not None and number_elem.text.strip() == target_number:
                incoming_elem = group.find("./timingExbytes/incoming")
                if incoming_elem is not None:
                    logging.info(
                        f"Значення incoming для group/number = {target_number}: {incoming_elem.text}"
                    )
                    return incoming_elem.text
                else:
                    logging.warning(
                        f"У групі з number={target_number} немає 'timingExbytes/incoming'."
                    )
                    return None

        logging.warning(f"Групу з number={target_number} не знайдено.")
        return None

    except ET.ParseError as e:
        logging.error(f"Помилка при парсингу XML: {e}")
    except FileNotFoundError:
        logging.error("Файл не знайдено.")
    except Exception as e:
        logging.error(f"Неочікувана помилка: {e}")


#  Виклик функції
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "groups.xml"))
find_incoming_value(file_path, "1203174")
