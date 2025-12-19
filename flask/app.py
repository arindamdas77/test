from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "pipline test part 2 Flask Backend part 2!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

