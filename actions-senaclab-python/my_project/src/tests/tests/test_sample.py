import unittest
from my_project import hello

class TestSample(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()