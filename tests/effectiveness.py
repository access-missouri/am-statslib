"""
ACCESS MISSOURI STATS LIBRARY - EFFECTIVENESS UNIT TESTS

"""

import unittest

from amstats import effectiveness


class EffectivenessTests(unittest.TestCase):
    def setUp(self):
        self.leg_zero = {
            "bills_introduced": 0,
            "actions_committee": 0,
            "beyond_committee": 0,
            "bills_passed": 0,
            "bills_law": 0
        }

        self.cohort_zero = {
            "bills_introduced": 0,
            "actions_committee": 0,
            "beyond_committee": 0,
            "bills_passed": 0,
            "bills_law": 0,
            "total": 0
        }

    def test_value_error_none_type(self):
        with self.assertRaises(ValueError):
            effectiveness.calculate_effectiveness(None, None)

    def test_value_error_no_cohort(self):
        with self.assertRaises(ValueError):
            effectiveness.calculate_effectiveness(self.leg_zero, self.cohort_zero)
