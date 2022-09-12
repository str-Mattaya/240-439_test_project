import unittest
from src.funny_string import *

class TestFunnyString(unittest.TestCase):

    def test_give_acxz_return_funny(self):
        text = 'acxz'
        expect = 'Funny'
        result = funny_string(text)
        self.assertEqual(result, expect)
    
    def test_give_bcxz_return_not_funny(self):
        text = 'bcxz'
        expect = 'Not Funny'
        result = funny_string(text)
        self.assertEqual(result, expect)
