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
    # Safety checks.
    if type(legislator) is not dict:
        raise ValueError("Legislator information must be stored in a dict as specified.")
    elif type(cohort) is not dict:
        raise ValueError("Cohort information must be stored in a dict as specified.")
    elif cohort['total'] < 1:
        raise ValueError("Cohort must have a population.")

    ratios = []

    ratios.append(float(legislator["bills_introduced"])/float(cohort["bills_introduced"]))
    ratios.append(float(legislator["actions_committee"]) / float(cohort["actions_committee"]))
    ratios.append(float(legislator["beyond_committee"]) / float(cohort["beyond_committee"]))
    ratios.append(float(legislator["bills_passed"]) / float(cohort["bills_passed"]))
    ratios.append(float(legislator["bills_law"]) / float(cohort["bills_law"]))

    answer = sum(ratios) * (cohort["total"]/5.0)

    return float("{0:.4f}".format(answer))


    raise NotImplementedError('Legislator Effectiveness calculation is still a work in progress.')