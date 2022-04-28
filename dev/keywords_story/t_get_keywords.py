from get_keywords import get_keywords
import unittest


class TestSolve(unittest.TestCase):
    def test_base(self):
        self.assertCountEqual(["в меру", "упитанный"], get_keywords("в меру упитанный"))

    def test_smth(self):
        # INSERT YOUR CODE HERE
        pass
