
import unittest
from zodiac_utils import panduan_xingzuo, pipei

class TestZodiacUtils(unittest.TestCase):
    def test_shuangzi(self):
        jieguo = panduan_xingzuo("06-06")
        self.assertEqual(jieguo["name"], "Gemini")

    def test_pipei_nan(self):
        jieguo = pipei("06-06", "male")
        self.assertEqual(jieguo["zodiac"], "Gemini")
        self.assertIn("talkative", jieguo["personality"])

    def test_pipei_nv(self):
        jieguo = pipei("06-06", "female")
        self.assertEqual(jieguo["zodiac"], "Gemini")
        self.assertIn("Lively", jieguo["personality"])

    def test_bianjie(self):
        jieguo = panduan_xingzuo("03-21")
        self.assertEqual(jieguo["name"], "Aries")

if __name__ == "__main__":
    unittest.main()
