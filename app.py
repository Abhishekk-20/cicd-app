from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        message="CI/CD Demo Application",
        status="running",
        version="1.0.1",
    ), 200


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


@app.get("/api/info")
def info():
    return jsonify(
        application="cicd-app",
        description="Flask application deployed using CI/CD and GitOps",
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
