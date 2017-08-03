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

    def test_integration_execution(self):
        expected_output = ['1', '2', 'Fizz', '4', 'Buzz']

        for count in range(1, 6):
            fizzbuzz = FizzBuzz(count)
            self.assertEquals(expected_output[count-1], fizzbuzz.execute())

        list_of_numbers = [15, 30, 45, 60]
        expected_output = 'FizzBuzz'

        for x in list_of_numbers:
            fizzbuzz = FizzBuzz(x)
            self.assertEquals('FizzBuzz', fizzbuzz.execute())


if __name__ == '__main__':
    unittest.main()
