from flask import Flask, redirect, url_for
from blueprints.detect import app as detect_blueprint
from blueprints.haarcascades import app as haarcascades_blueprint

app = Flask(__name__)
app.register_blueprint(detect_blueprint)
app.register_blueprint(haarcascades_blueprint)


@app.route("/")
def index():
    return redirect(url_for("haarcascades.index"))


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)
