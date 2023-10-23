import funcs
import unittest

class TestSum(unittest.TestCase):
    def test_char(self):
        with self.assertRaises(TypeError):
            funcs.joeaddition("a", "b")

if __name__ == '__main__':
    unittest.main()