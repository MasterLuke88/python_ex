import unittest
from calculator import *

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(multip(2,2), 4)
	self.assertEqual(multip(7,9),63)
	self.assertEqual(multip(-2,6),-12)

if __name__ == '__main__':
    unittest.main()
