"""
Think Stats Exercise 2-7.

1. Compute the conditional probability that a baby will be born in Week 39,
given that it was not born prior to Week 39.
2. Extend this to compute the probability that a baby will be born during
Week x, given that it was not born prior to Week x.
3. Plot this value as a function of x for first babies and others.
"""
import sys

import Pmf
import survey

import utils

# On first blush, this is really just another survival analysis problem. So
# we build a Pmf.Pmf for babies' births and use the same kind of analysis
# as we did for Exercise 2-4.
if __name__ == '__main__':
    data_dir = sys.argv[1]
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    
    # Part 1
    live_pmf = Pmf.MakePmfFromList([prg.prglength for prg in table.records])
    new_pmf = utils.remaining_lifetime(live_pmf, 38)
    print 'Probability that a live birth will be in Week 39 if not born '\
        'prior to Week 39:', new_pmf.Prob(38)
        
    # Part 2 isn't really a meaningful task if I'm right in my approach of
    # using the survival analysis approach, since then Part 1 was just a
    # special use case. Let's demonstrate some usage.
    new_pmf = utils.remaining_lifetime(live_pmf, 24)
    print 'Probability that a live birth will be in Week 25 if not born '\
        'prior to Week 39:', new_pmf.Prob(24)

    new_pmf = utils.remaining_lifetime(live_pmf, 49)
    print 'Probability that a live birth will be in Week 50 if not born '\
        'prior to Week 39:', new_pmf.Prob(49)