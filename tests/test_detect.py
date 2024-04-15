import numpy as np
import unittest
import main


class TestError(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def test_no_data(self):
        headers = {'Content-Type': 'image/jpeg'}
        response = self.app.post("/detect/face", headers=headers)
        self.assertEqual(response.status_code, 400)

    def test_invalid_haarcascade(self):
        headers = {'Content-Type': 'image/jpeg'}
        response = self.app.post("/detect/hi", data=np.array([]).tobytes(), headers=headers)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
