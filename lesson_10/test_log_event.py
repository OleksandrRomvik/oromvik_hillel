import pytest
import logging
from lesson_10.homework_10 import (
    log_event,
)  # заміни на актуальну назву модуля або залиш так, якщо все в одному файлі


@pytest.mark.parametrize(
    "status,expected_level",
    [
        ("success", logging.INFO),
        ("expired", logging.WARNING),
        ("failed", logging.ERROR),
        ("unknown", logging.ERROR),  # додатковий кейс
    ],
)
def test_log_event_logging_levels(caplog, status, expected_level):
    username = "test_user"
    expected_msg = f"Login event - Username: {username}, Status: {status}"

    # caplog дозволяє захопити повідомлення логера
    with caplog.at_level(logging.DEBUG):  # охоплює всі рівні
        log_event(username, status)

    # Шукаємо повідомлення у caplog.records
    messages = [record for record in caplog.records if expected_msg in record.message]
    assert len(messages) == 1, f"Очікували один запис логів для статусу '{status}'"
    assert messages[0].levelno == expected_level
