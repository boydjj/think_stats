"""
Think Stats Exercise 2-1.

Compute the mean, variance, and standard deviation of the text's described
pumpkin weights.
"""

import thinkstats
from utils import std_dev

def pumpkin(weights):
    """
    Given an iterable of pumpkin weights, compute the sequence's mean,
    variance, and standard deviation.
    """
    mean = thinkstats.Mean(weights)
    variance = thinkstats.Var(weights, mean)
    stddev = std_dev(weights, mean, variance)

    return mean, variance, stddev

if __name__ == '__main__':
    # From the text: the weights of the pumpkins we've harvested.
    weights = (1, 1, 1, 3, 3, 591)
    mean, variance, stddev = pumpkin(weights)

    print "The mean pumpkin weight is:", mean
    print "The pumpkin weight variance is:", variance
    print "The pumpkin weight standard deviation is:", stddev