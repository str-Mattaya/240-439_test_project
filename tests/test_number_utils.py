import unittest
from src.number_utils import *


class PrimeListTest(unittest.TestCase):
    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_10_is_not_prime(self):
        prime_list = [4,6,10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_9_15_21_is_not_prime(self):
        prime_list = [9,15,21]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_0_1_is_not_prime(self):
        prime_list = [0,1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_neg_2_3_5_7_is_prime(self):
        prime_list = [-2,-3,-5,-7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_neg_4_1_9_15_is_not_prime(self):
        prime_list = [-4,-1,-9,-15]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

