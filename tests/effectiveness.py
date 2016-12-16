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

        self.schaefer_fifteen = {
            "bills_introduced": 27,
            "actions_committee": 27,
            "beyond_committee": 24,
            "bills_passed": 5,
            "bills_law": 2
        }

        self.cohort_fifteen = {
            "bills_introduced": 1633,
            "actions_committee": 606,
            "beyond_committee": 269,
            "bills_passed": 265,
            "bills_law": 62,
            "total": 34
        }

    def test_value_error_none_type(self):
        with self.assertRaises(ValueError):
            effectiveness.calculate_effectiveness(None, None)

    def test_value_error_none_cohort(self):
        with self.assertRaises(ValueError):
            effectiveness.calculate_effectiveness(self.leg_zero, None)

    def test_value_error_no_cohort(self):
        with self.assertRaises(ValueError):
            effectiveness.calculate_effectiveness(self.leg_zero, self.cohort_zero)

    def test_schaefer_fifteen(self):
        self.longMessage = True
        self.assertEqual(effectiveness.calculate_effectiveness(self.schaefer_fifteen, self.cohort_fifteen), 1.3697,
                         "Unexpected answer.")
