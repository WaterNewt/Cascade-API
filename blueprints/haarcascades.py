import json
from flask import Blueprint, send_file, request

app = Blueprint("haarcascades", __name__)


@app.route('/haarcascades/')
def index():
    cascade_file = request.args.get("file", None, str)
    print(cascade_file)
    with open("haarcascades.json", "r") as f:
        haarcascades = json.load(f)
    available_files = [i.split("/")[1] for i in haarcascades.values()]
    if cascade_file is not None:
        if cascade_file in available_files:
            try:
                return send_file("haarcascades/"+cascade_file, as_attachment=True), 200
            except FileNotFoundError:
                return {"code": 404, "error": "Could not find cascade file"}, 404
        else:
            return {"code": 404, "error": "Invalid haarcascade file"}, 404
    return haarcascades, 200
