from flask import Flask, request, jsonify

app = Flask(__name__)

BLACKLIST = ["chatgpt", "gemini", "discord"]

@app.route("/keywords", methods=["GET"])
def get_keywords():
    return jsonify(BLACKLIST)

@app.route("/keywords", methods=["POST"])
def update_keywords():
    global BLACKLIST
    data = request.json
    if isinstance(data, list):
        BLACKLIST = [str(k).lower() for k in data]
        return {"status": "updated", "keywords": BLACKLIST}
    return {"error": "invalid"}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
