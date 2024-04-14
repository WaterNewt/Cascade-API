import cv2
import json
import numpy as np
from flask import Blueprint, request, jsonify

with open("haarcascades.json", "r") as f:
    haarcascades: dict[str, str] = json.load(f)
app = Blueprint("face", __name__)


@app.route("/detect/<haarcascade>", methods=['POST'])
def detect(haarcascade):
    nparr = np.fromstring(request.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if haarcascade not in haarcascades.keys():
        return {"code": 400, "error": "Invalid haarcascade. Go to /haarcascades for all the haarcascades"}
    cascade = cv2.CascadeClassifier(haarcascades[haarcascade])
    face_rects = cascade.detectMultiScale(img, 1.3, 5)
    if len(face_rects) > 0:
        face_rects = [i.tolist() for i in face_rects]

    return jsonify(face_rects), 200
