# Cascade API
A simple API written in Python for object detection with haarcascades

## Important notes
- This project is just a personal project.
- If you would like to do anything that goes against the license (GPL-3.0), please contact me.

## Run
- Install the required dependencies: `pip3 install -r requirements.txt`
- Run the application: `python3 main.py`. The main script will import all the blueprints and run the API
- (Optional): Run the example script in a seperate terminal: `python3 example.py`

## Example class:
```python
import cv2
import requests


class CascadeClient:
    def __init__(self, image: str = None, host: str = "http://localhost:5000", cascade: str = "face"):
        self.host = host
        if image is None:
            raise ValueError("Please provide an image")
        self.image = image
        self.cascade = cascade
        self.detect_url = host+'/detect/'+self.cascade

    def get_rectangles(self):
        headers = {'Content-Type': 'image/jpeg'}

        img = cv2.imread(self.image)
        _, img_encoded = cv2.imencode('.png', img)

        rectangles = requests.post(self.detect_url, data=img_encoded.tobytes(), headers=headers)
        return rectangles.json()
```

## License
This project is under the GPL-3.0 license. Read more [here](LICENSE)