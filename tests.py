import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_is_divisible_by_three(self):
        fizzbuzz = FizzBuzz()
        self.assertTrue(fizzbuzz.number_divisible_by_three(3))
        self.assertFalse(fizzbuzz.number_divisible_by_three(4))

    def test_number_is_divisible_by_five(self):
        fizzbuzz = FizzBuzz()

        self.assertTrue(fizzbuzz.number_divisible_by_five(5))
        self.assertFalse(fizzbuzz.number_divisible_by_five(6))

    def test_number_is_divisible_by_three_and_five(self):
        fizzbuzz = FizzBuzz()

        self.assertTrue(fizzbuzz.number_divisible_by_three(15) and
                        fizzbuzz.number_divisible_by_five(15))


if __name__ == '__main__':
    unittest.main()
