from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No file"}), 400
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return jsonify({"image_url": f"http://127.0.0.1:8080/uploads/{file.filename}"}), 201


@app.route("/image/<filename>", methods=["GET"])
def get_image(filename):
    # За заголовком визначаємо, що повертати (JSON чи сам файл)
    if request.headers.get("Accept") == "text":
        return jsonify({"image_url": f"http://127.0.0.1:8080/uploads/{filename}"})
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/delete/<filename>", methods=["DELETE"])
def delete(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({"image_url": f"http://127.0.0.1:8080/uploads/{filename}"})
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
