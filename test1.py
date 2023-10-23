import funcs
import unittest


class test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(funcs.joeaddition(1,2), 3)
if __name__ == 'main':
    unittest.main()
