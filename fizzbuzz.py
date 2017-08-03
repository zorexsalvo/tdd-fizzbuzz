class FizzBuzz:
    def __init__(self, number=0):
        self.number = number

    def number_divisible_by_three(self, number):
        return number % 3 == 0

    def number_divisible_by_five(self, number):
        return number % 5 == 0

    def execute(self):
        if (self.number_divisible_by_three(self.number) and
            self.number_divisible_by_five(self.number)):
            return 'FizzBuzz'

        elif self.number_divisible_by_three(self.number):
            return 'Fizz'

        elif self.number_divisible_by_five(self.number):
            return 'Buzz'

        else:
            return '{}'.format(self.number)


for count in xrange(1,100):
    fizzbuzz = FizzBuzz(count)
    print(fizzbuzz.execute())
