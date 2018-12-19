import unittest
from sample import add

class TestSample(unittest.TestCase):

    def test_add(self):
        value1 = 2
        value2 = 4

        expected = 6
        actual = add(value1, value2)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()