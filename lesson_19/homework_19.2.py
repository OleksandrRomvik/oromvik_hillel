import requests
from urllib.parse import urlparse

# ТУТ ВКАЖІТЬ ТОЙ САМИЙ ХОСТ І ПОРТ, НА ЯКОМУ СТАРТУВАВ ВАШ Flask-СЕРВЕР
BASE_URL = "http://127.0.0.1:8080"


def upload_image(path_to_file: str) -> str:
    """
    1) Відправляє POST /upload з полем 'image' — файл.
    2) Очікує статус 201 і повертає data['image_url'].
    """
    with open(path_to_file, "rb") as f:
        files = {"image": f}
        resp = requests.post(f"{BASE_URL}/upload", files=files)
    resp.raise_for_status()  # якщо код ≠201, винесе виключення
    return resp.json()["image_url"]


def get_image_url(filename: str) -> str:
    """
    1) Робить GET /image/<filename> з заголовком Accept: text
    2) Очікує статус 200 і повертає data['image_url'].
    """
    headers = {"Accept": "text"}
    resp = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
    resp.raise_for_status()
    return resp.json()["image_url"]


def delete_image(filename: str) -> None:
    """
    1) Робить DELETE /delete/<filename>
    2) Очікує статус 200 і друкує повернений JSON.
    """
    resp = requests.delete(f"{BASE_URL}/delete/{filename}")
    resp.raise_for_status()
    print("DELETE response:", resp.json())


def main():
    # 1) Вкажіть тут існуюче зображення у тій самій папці, де лежить client.py
    local_file = "example.jpg"

    print(f'1) Uploading "{local_file}"…')
    uploaded_url = upload_image(local_file)
    print("   → Uploaded URL:", uploaded_url)

    # 2) Витягуємо імя файлу з URL (після останнього '/')
    filename = urlparse(uploaded_url).path.rsplit("/", 1)[-1]

    print(f'2) Fetching info for "{filename}"…')
    info_url = get_image_url(filename)
    print("   → GET returned image_url:", info_url)

    print(f'3) Deleting "{filename}"…')
    delete_image(filename)
    print("   → Done.")


if __name__ == "__main__":
    main()
