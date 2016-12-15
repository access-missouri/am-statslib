"""
Legislator Effectiveness Scores
Uses an adaptation of Volden-Washington's method for calculating legislator effectiveness to calculate scores.

Created: December 2016
Updated: December 2016
Author: Nathan Lawrence
"""


def calculate_effectiveness(legislator, cohort):
    """
    Calculate the legislative effectiveness score given a single legislator and their cohort as dicts.

    Args:
        legislator: Dict with attributes (as int)-
            bills_introduced (bills introduced into legislature),
            actions_committee (bills introduced that had actions in committee),
            beyond_committee (bills introduced that had actions beyond committee),
            bills_passed (bills introduced that passed the legislator's parent chamber),
            bills_law (bills that were perfected and/or signed).
        cohort: Dict with attributes (as int)-
            total (number of all legislators in subject's parent chamber)
            bills_introduced (bills introduced into legislature by all legislators in subject's parent chamber),
            actions_committee (bills introduced that had actions in committee for all legs),
            beyond_committee (bills introduced that had actions beyond committee for all legs),
            bills_passed (bills introduced that passed the legislator's parent chamber for all legs),
            bills_law (bills that were perfected and/or signed for all legs).

    """
    raise NotImplementedError('Legislator Effectiveness calculation is still a work in progress.')