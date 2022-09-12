import unittest
from src.alternating_characters import *


class TestAlternatingCharacters(unittest.TestCase):

    def test_give_AABAAB_return_2(self):
        text = 'AABAAB'
        expect = 2
        result = alternating_characters(text)
        self.assertEqual(expect, result)
    
    def test_give_AAAA_return_3(self):
        text = 'AAAA'
        expect = 3
        result = alternating_characters(text)
        self.assertEqual(expect, result)
    
    def test_give_BBBBB_return_4(self):
        text = 'BBBBB'
        expect = 4
        result = alternating_characters(text)
        self.assertEqual(expect, result)
    
    def test_give_ABABABAB_return_0(self):
        text = 'ABABABAB'
        expect = 0
        result = alternating_characters(text)
        self.assertEqual(expect, result)
    
    def test_give_BABABA_return_0(self):
        text = 'BABABA'
        expect = 0
        result = alternating_characters(text)
        self.assertEqual(expect, result)
    
    def test_give_AAABBB_return_4(self):
        text = 'AAABBB'
        expect = 4
        result = alternating_characters(text)
        self.assertEqual(expect, result)
