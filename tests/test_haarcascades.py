import unittest
import json
import main


class TestResponse(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def test_json(self):
        response = self.app.get("/haarcascades/")
        with open("haarcascades.json", "r") as f:
            self.assertEqual(response.json, json.load(f))

    def test_file(self):
        response = self.app.get("/haarcascades/?file=haarcascade_fullbody.xml")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
