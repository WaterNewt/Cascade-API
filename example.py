import requests
import cv2

haarcascade = "face"
url = "http://localhost:5000/detect/"+haarcascade
headers = {'Content-Type': 'image/jpeg'}

img = cv2.imread('kanye_west.jpg')
_, img_encoded = cv2.imencode('.png', img)

rectangles = requests.post(url, data=img_encoded.tobytes(), headers=headers)
print(rectangles.json())
for (x, y, w, h) in rectangles.json():
    cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
