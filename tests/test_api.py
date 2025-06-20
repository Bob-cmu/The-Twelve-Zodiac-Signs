
import unittest
import json
from app import app

class TestZodiacAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_post_match(self):
        shuju = {"birthday": "06-06", "gender": "male"}
        fanhui = self.client.post("/match", json=shuju)
        self.assertEqual(fanhui.status_code, 200)
        shuju = fanhui.get_json()
        self.assertEqual(shuju["zodiac"], "Gemini")
        self.assertIn("talkative", shuju["personality"])

if __name__ == "__main__":
    unittest.main()
