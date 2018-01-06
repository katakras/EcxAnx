import unittest

import numpy
import ar1

class MyTestCase(unittest.TestCase):

    # tests that something is actually being run
    def test_basic(self):
        self.assertEqual(True, True)

    def test_accuracy(self):
        self.assertAlmostEqual(1.00002, 1.00003, 3)
    def test_ar1(self):
        numpy.random.seed(0)
        result = ar1.eleni(1,0.5,0.5,8)
        self.assertAlmostEqual(result[-1],1.5034877815517456,6)
        self.assertEqual(len(result),9)


if __name__ == '__main__':
    unittest.main()
