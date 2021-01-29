"""
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
tests should pass. Also include a test that does not pass.

NOTE: You can write both the code as well as the tests for it in this single file.
However, feel free to adhere to best practices and separate your tests and the functions you are testing
into different files. Note that you will run into an error when attempting to import this file,
because Python modules can't begin with a number.

"""

import unittest
from firststep import y


class MyTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(y, 625)

    def test_more_than_zero(self):
        self.assertTrue((y > 0))

    def test_integer_or_not(self):
        self.assertIsInstance(y, int)
# failing test:

    def test_identity(self):
        self.assertIs(y, 625, msg=f'{y} is not 625')


if __name__ == '__main__':
    unittest.main()
