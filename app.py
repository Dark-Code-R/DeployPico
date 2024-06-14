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
    with open("archivo_lista.txt", "w") as file:
        file.write(content)

    return jsonify({"message": "Data received and saved"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
