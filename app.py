from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Updated again API "})

@app.route("/user")
def user():
    return jsonify({"name": "Priya", "role": "DevOps learner"})

app.run(host="0.0.0.0", port=5000)
