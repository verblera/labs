"""
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

"""

# function x / z

import unittest
from secondtest import x, z


class MyTest(unittest.TestCase):

    def test_not_zero(self):
        self.assertNotEqual(z, 0)

    def test_existence(self):
        self.assertIsNotNone(z)
        self.assertIsNotNone(x)

    def test_integer_or_not(self):
        self.assertIsInstance(z, int)
        self.assertIsInstance(x, int)

if __name__ == '__main__':
    unittest.main()
