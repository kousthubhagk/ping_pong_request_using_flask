from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.get_json()  # Get the input data from Postman request
    if data and data.get("input") == "ping":
        return jsonify({"output": "pong"}), 200
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
