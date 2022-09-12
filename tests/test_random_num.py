import unittest
from unittest import mock
import src.random_num as random_num


class TestRandomNum(unittest.TestCase):
    
    @mock.patch('random.randint', return_value=2)
    def test_mock_guess_int_return_2(self, guess_int_mock):
        start = 1 ; stop = 2
        expect = 2
        guess_int_mock()
        result = random_num.guess_int(start, stop)
        self.assertEqual(result, expect)
    
    @mock.patch('random.uniform', return_value=3.14)
    def test_mock_guess_float_return_3p14(self, guess_float_mock):
        start = 1.2 ; stop = 6.4
        expect = 3.14
        guess_float_mock()
        result = random_num.guess_float(start, stop)
        self.assertEqual(result, expect)
