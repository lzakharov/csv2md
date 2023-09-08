from unittest import TestCase

from .utils import column_letter


class TestUtils(TestCase):
    def test_column_letter(self):
        self.assertEqual(column_letter(0), 'a')
        self.assertEqual(column_letter(4), 'e')
        self.assertEqual(column_letter(30), 'ee')
