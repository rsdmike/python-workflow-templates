import unittest
from main import HelloWorld

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = HelloWorld()
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()