from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "I am a basic Flask app that goes: DING! 🛎"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
