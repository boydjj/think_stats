"""
Think Stats Exercise 2-7.

1. Compute the conditional probability that a baby will be born in Week 39,
given that it was not born prior to Week 39.
2. Extend this to compute the probability that a baby will be born during
Week x, given that it was not born prior to Week x.
3. Plot this value as a function of x for first babies and others.
"""
import sys
from matplotlib import pyplot

import survey
import descriptive

from my_first import partition_births
import utils


def _print_survival_analysis(week, table, label):
    new_pmf = utils.remaining_lifetime(table.pmf, week)
    print 'Probability that a live birth will be in Week {week_num} if not born '\
        'prior to Week {week_num} ({label}):'.format(week_num=week, label=label),\
        new_pmf.Prob(week)

# On first blush, this is really just another survival analysis problem. So
# we build a Pmf.Pmf for babies' births and use the same kind of analysis
# as we did for Exercise 2-4 using utils.remaining_lifetime.
if __name__ == '__main__':
    data_dir = sys.argv[1]
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    firsts, others = partition_births(table)

    descriptive.Process(firsts, 'firsts')
    descriptive.Process(others, 'others')

    # Part 1 - conditional probability that a baby will be born in week 39
    # Relevant output from official code:
    # 39 0.633693045564 first babies
    # 39 0.715792395226 others
    _print_survival_analysis(39, firsts, 'firsts')
    _print_survival_analysis(39, others, 'others')

    # Part 2 isn't really a meaningful task if we're right to just use
    # the survival analysis approach. In that case, Part 1 was just a
    # special use case. Let's demonstrate this.

    # Relevant output from official code:
    # 41 0.524781341108 first babies
    # 41 0.511261261261 others
    _print_survival_analysis(41, firsts, 'firsts')
    _print_survival_analysis(41, others, 'others')


    pyplot.clf()
