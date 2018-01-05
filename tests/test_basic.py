import unittest


class MyTestCase(unittest.TestCase):

    # tests that something is actually being run
    def test_basic(self):
        self.assertEqual(True, True)

    def test_accuracy(self):
        self.assertAlmostEqual(1.00002, 1.00003, 3)


if __name__ == '__main__':
    unittest.main()
