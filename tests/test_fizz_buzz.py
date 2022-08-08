import unittest
from fizz_buzz.fizz_buzz import is_fizz_or_buzz


class FizzBuzzTest(unittest.TestCase):

    def test_give_neg1_return_nothing(self):
        num = -1
        result = is_fizz_or_buzz(num)
        expect = ''
        self.assertEqual(result, expect)
    
    def test_give_0_return_nothing(self):
        num = 0
        result = is_fizz_or_buzz(num)
        expect = ''
        self.assertEqual(result, expect)
    
    def test_give_1_return_nothing(self):
        num = 0
        result = is_fizz_or_buzz(num)
        expect = ''
        self.assertEqual(result, expect)

    def test_give_999_return_fizz(self):
        num = 999
        result = is_fizz_or_buzz(num)
        expect = 'Fizz'
        self.assertEqual(result, expect)
    
    def test_give_1000_return_buzz(self):
        num = 1000
        result = is_fizz_or_buzz(num)
        expect = 'Buzz'
        self.assertEqual(result, 'Buzz')

    def test_give_1001_return_nothing(self):
        num = 0
        result = is_fizz_or_buzz(num)
        expect = ''
        self.assertEqual(result, expect)
    
    def test_give_15_return_fizzbuzz(self):
        num = 15
        result = is_fizz_or_buzz(num)
        expect = 'FizzBuzz'
        self.assertEqual(result, expect)
    
    def test_give_450_return_fizzbuzz(self):
        num = 450
        result = is_fizz_or_buzz(num)
        expect = 'FizzBuzz'
        self.assertEqual(result, expect)
    
    def test_give_500_return_Buzz(self):
        num = 500
        result = is_fizz_or_buzz(num)
        expect = 'Buzz'
        self.assertEqual(result, expect)
    
    def test_give_501_return_Fizz(self):
        num = 501
        result = is_fizz_or_buzz(num)
        expect = 'Fizz'
        self.assertEqual(result, expect)
    
    def test_give_499_return_nothing(self):
        num = 499
        result = is_fizz_or_buzz(num)
        expect = ''
        self.assertEqual(result, expect)
    