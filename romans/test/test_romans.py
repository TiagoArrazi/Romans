import unittest
from src.utils.roman import Roman


class TestRomans(unittest.TestCase):

    def test_equal_1(self):
        self.assertEqual(Roman.convert_digits('1'), 'I')

    def test_equal_2(self):
        self.assertEqual(Roman.convert_digits('200'), 'CC')

    def test_equal_3(self):
        self.assertEqual(Roman.convert_digits('1700'), 'MDCC')

    def test_equal_4(self):
        self.assertEqual(Roman.convert_digits('2998'), 'MMCMXCVIII')

    def test_false_1(self):
        self.assertFalse(Roman.convert_digits('0'))

    def test_false_2(self):
        self.assertFalse(Roman.convert_digits('3001'))

    def test_false_3(self):
        self.assertFalse(Roman.convert_digits('ABC'))