import unittest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from filters.filters import Filters


class TestTypesMethods(unittest.TestCase):

    def test_integer(self):
        self.assertTrue(Filters().is_integer(45))
        self.assertFalse(Filters().is_integer("45"))

    def test_str(self):
        self.assertTrue(Filters().is_str("45"))
        self.assertFalse(Filters().is_str(45))

    def test_list(self):
        self.assertTrue(Filters().is_list([]))
        self.assertFalse(Filters().is_list(45))
        self.assertFalse(Filters().is_list({}))


if __name__ == '__main__':
    unittest.main()
