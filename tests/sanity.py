"""
ACCESS MISSOURI STATS LIBRARY - SANITY UNIT TESTS

"""

import unittest

import amstats.effectiveness

class SanityTests(unittest.TestCase):
    def test_sanity(self):
        assert 1 + 1 == 2

    def test_sanity_again(self):
        assert 1 - 1 == 0