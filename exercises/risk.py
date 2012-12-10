"""
Think Stats Exercise 2-6.

Provide analysis over whether various groups of birth are likely
to be early, late, or on time.
"""
import functools
import sys

import Pmf
import survey
import my_first

def prob_in_weeks(pmf, start, end):
    prob_sum = 0
    for val, prob in pmf.Items():
        if start <= val <= end:
            prob_sum += prob
    return prob_sum

prob_early = functools.partial(prob_in_weeks, start=0, end=37)
prob_on_time = functools.partial(prob_in_weeks, start=38, end=40)
prob_late = functools.partial(prob_in_weeks, start=41, end=1000000)

if __name__ == '__main__':
    data_dir = sys.argv[1]
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    first_births, other_births = my_first.partition_births(table)

    live_pmf = Pmf.MakePmfFromList([prg.prglength for prg in table.records])
    first_pmf = Pmf.MakePmfFromList([prg.prglength for prg in first_births.records])
    other_pmf = Pmf.MakePmfFromList([prg.prglength for prg in other_births.records])

    prob_early_first = prob_early(first_pmf)
    prob_early_other = prob_early(other_pmf)

    print 'Early probability (all live):', prob_early(live_pmf) * 100
    print 'Early probability (firsts):', prob_early_first * 100
    print 'Early probability (others):', prob_early_other * 100
    print 'Relative risk of being early (first vs. other):', prob_early_first / prob_early_other
    print

    prob_on_time_first = prob_on_time(first_pmf)
    prob_on_time_other = prob_on_time(other_pmf)

    print 'On-time probability (all live):', prob_on_time(live_pmf) * 100
    print 'On-time probability (firsts):', prob_on_time_first * 100
    print 'On-time probability (others):', prob_on_time_other * 100
    print 'Relative risk of being on-time (first vs. other):', prob_on_time_first / prob_on_time_other
    print

    prob_late_first = prob_late(first_pmf)
    prob_late_other = prob_late(other_pmf)

    print 'Late probability (all live):', prob_late(live_pmf) * 100
    print 'Late probability (firsts):', prob_late_first * 100
    print 'Late probability (others):', prob_late_other * 100
    print 'Relative risk of being late (first vs. other):', prob_late_first / prob_late_other
