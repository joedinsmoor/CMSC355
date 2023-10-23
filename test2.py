import funcs
import unittest

class TestSum(unittest.TestCase):
    def test_char(self):
        self.assertNotEqual(funcs.joeaddition(1,2), 4)

if __name__ == '__main__':
    unittest.main()