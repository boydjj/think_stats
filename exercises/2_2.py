"""
Think Stats Exercise 2-2.

Compute the std. dev. of gestation time for first vs. other babies. (Added
bits about mean and variance for kicks.)

Assumes my project setup, so requires data directory in sys.argv. Example:
$ pwd
/path/to/think_stats
$ python exercises/2_2.py data/

See README.md for more info.
"""
import sys

from my_first import partition_births
import survey
from thinkstats import Mean, Var
from utils import std_dev


if __name__ == '__main__':
    data_dir = sys.argv[1]
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    firsts, others = partition_births(table)

    firsts_gestation_lengths = list((p.prglength for p in firsts.records))
    others_gestation_lengths = list((p.prglength for p in others.records))

    for births in (firsts, others):
        births_gestation_lengths = list((p.prglength for p in births.records))
        births.mean = Mean(births_gestation_lengths)
        births.variance = Var(births_gestation_lengths, births.mean)
        births.std_dev = std_dev(births_gestation_lengths, births.mean, births.variance)


    print 'The mean gestation time for firstborns is:', firsts.mean
    print 'The mean gestation time for others is:', others.mean

    print 'The gestation time variance for firstborns is:', firsts.variance
    print 'The gestation time variance for others is:', others.variance

    print 'The standard deviation of gestation times for firstborns is:', firsts.std_dev
    print 'The standard deviation of gestation times for others is:', others.std_dev
