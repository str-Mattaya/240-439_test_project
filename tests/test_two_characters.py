import unittest
from src.two_characters import *


class TestTwoCharacters(unittest.TestCase):

    def test_give_beabeefeab_return_5(self):
        text = 'beabeefeab'
        expect = 5
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_abaacdabd_return_4(self):
        text = 'abaacdabd'
        expect = 4
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_aaabaa_return_0(self):
        text = 'aaabaa'
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_a_return_0(self):
        text = 'a'
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_aa_return_0(self):
        text = 'aa'
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_nonestr_return_0(self):
        text = ''
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_abababab_return_8(self):
        text = 'abababab'
        expect = 8
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_ab_return_2(self):
        text = 'ab'
        expect = 2
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_aaaaaaa_return_0(self):
        text = 'aaaaaaa'
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    