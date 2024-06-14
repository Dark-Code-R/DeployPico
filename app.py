from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    content = data.get("content")
    if not content:
        return jsonify({"error": "No content provided"}), 400

    # Guarda el contenido en un archivo
    file_path = "archivo_lista.txt"
    with open(file_path, "w") as file:
        file.write(content)

    return jsonify({"message": "Data received and saved", "file_path": file_path}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
