from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Lotto API Live!"

@app.route("/lotto")
def lotto():
    data = {
        "date": "2026-04-19",
        "result": ["12", "34", "56"],
        "prediction": ["11", "22", "33"]
    }
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 
