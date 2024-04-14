import json
from flask import Blueprint, send_file, render_template

app = Blueprint("haarcascades", __name__)


@app.route("/haarcascades/")
@app.route('/haarcascades/<cascade_file>')
def index(cascade_file=None):
    if cascade_file is not None:
        return send_file("haarcascades/"+cascade_file, as_attachment=True)
    with open("haarcascades.json", "r") as f:
        return render_template("haarcascades.html", haarcascades=json.load(f))
