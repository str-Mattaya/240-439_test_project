from cmath import exp
import unittest
from src.caesar_cipher import *


class TestCaesarCipher(unittest.TestCase):

    def test_give_abcdefghijklmnopqrstuvwxyz_step_2_return_cdefghijklmnopqrstuvwxyzab(self):
        text = 'abcdefghijklmnopqrstuvwxyz' ; step = 2
        expect = 'cdefghijklmnopqrstuvwxyzab'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)
    
    def test_give_abcdefghijklmnopqrstuvwxyz_step_26_return_abcdefghijklmnopqrstuvwxyz(self):
        text = 'abcdefghijklmnopqrstuvwxyz' ; step = 26
        expect = 'abcdefghijklmnopqrstuvwxyz'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)
    
    def test_give_abcdefghijklmnopqrstuvwxyz_step_n1_return_zabcdefghijklmnopqrstuvwxy(self):
        text = 'abcdefghijklmnopqrstuvwxyz' ; step = -1
        expect = 'zabcdefghijklmnopqrstuvwxy'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)
    
    def test_give_middleOutz_step_2_return_okffngQwvb(self):
        text = 'middle-Outz' ; step = 2
        expect = 'okffng-Qwvb'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)
    