from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "I am a buildpack-powered Flask app that goes: DING! 🛎\n"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
