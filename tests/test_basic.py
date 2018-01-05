import unittest


class MyTestCase(unittest.TestCase):

    # tests that something is actually being run
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
