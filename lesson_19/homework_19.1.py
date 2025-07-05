import requests

# 1. Збираємо дані для запиту
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {"sol": 1000, "camera": "fhaz", "api_key": "DEMO_KEY"}

# 2. Виконуємо GET-запит
response = requests.get(url, params=params)
response.raise_for_status()  # перевіряємо, що запит успішний

data = response.json()

# 3. Отримуємо список об’єктів photo
photos = data.get("photos", [])
if not photos:
    print("Фотографій не знайдено.")
    exit(1)

# 4. Завантажуємо і зберігаємо перші дві фотографії
for idx, photo in enumerate(photos[:2], start=1):
    img_url = photo.get("img_src")
    if not img_url:
        print(f"Фото #{idx} — посилання не знайдено.")
        continue

    # робимо запит на саму картинку
    img_resp = requests.get(img_url, stream=True)
    img_resp.raise_for_status()

    # зберігаємо файл
    filename = f"mars_photo{idx}.jpg"
    with open(filename, "wb") as f:
        for chunk in img_resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Збережено {filename}")
