import unittest
from KMPmethod import *


class TestCipher(unittest.TestCase):
    def test_1(self):
        test = KMP_method()
        self.assertEqual(test.kmp('ababbabab', 'abb'), 2)

    def test_2(self):
        test = KMP_method()
        self.assertEqual(test.kmp('ababbabab', ''), 0)

    def test_3(self):
        test = KMP_method()
        self.assertEqual(test.kmp('', 'abb'), None)

    def test_4(self):
        test = KMP_method()
        self.assertEqual(test.kmp('ababbabab', 'aaacc'), None)

    def test_5(self):
        test = KMP_method()
        self.assertNotEqual(test.kmp('ababbabab', 'abb'), 3)