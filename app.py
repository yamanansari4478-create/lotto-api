from flask import Flask, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Lotto API Live!"

@app.route("/lotto")
def lotto():
    numbers = [str(random.randint(10, 99)) for _ in range(3)]
    prediction = [str(random.randint(10, 99)) for _ in range(3)]

    data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "result": numbers,
        "prediction": prediction
    }

    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
