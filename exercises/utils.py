"""
Think Stats, many Exercises.

Here I'll keep any utility that looks to be of general purpose as I go through
the book. Will try to document each util with the exercise for which I wrote
it.
"""

import math
import operator

import thinkstats

def std_dev(seq, mean=None, var=None):
    if not var:
        var = thinkstats.Var(seq, mean)

    return math.sqrt(var)
    
def mode(hist):
    """
    Think Stats Exercise 2-3.
    
    Given a Pmf.Hist object, find the mode of its values.
    """
    max_freq = None
    mode = None
    for val, freq in hist.Items():
        if freq > max_freq:
            max_freq = freq
            mode = val
    return mode

def all_modes(hist):
    """
    Think Stats Exercise 2-3.
    
    Given a Pmf.Hist object, return a list of (value, frequency) pairs
    in descending order of frequency.
    """
    freq_getter = operator.itemgetter(1)
    return sorted(hist.Items(), key=freq_getter, reverse=True)

def remaining_lifetime(pmf, age):
    """
    Think Stats Exercise 2-4.
    
    Given a Pmf.Pmf object of lifetimes and an age, return a new Pmf.Pmf that
    represents the distribution of remaining lifetimes.
    
    Example pop data: [1, 2, 2, 3, 3, 3, 3, 4, 5]
    """
    new_pmf = pmf.Copy()
    for val in pmf.Values():
        if val < age:
            new_pmf.Remove(val)
    new_pmf.Normalize()
    return new_pmf

def pmf_mean(pmf):
    """
    Think Stats Exercise 2-5.
    
    Given a Pmf.Pmf object, compute the mean of its values.
    """
    return sum([val * prob for val, prob in pmf.Items()])

def pmf_var(pmf):
    """
    Think Stats Exercise 2-5.
    
    Given a Pmf.Pmf object, compute the variance of its values.
    """    
    # var = 0
    # mean = pmf_mean(pmf)
    # for val, prob in pmf.Items():
    #     dev = val - mean
    #     var += prob * dev**2
    # return var
    mean = pmf_mean(pmf)
    return sum([prob * (val-mean)**2 for val, prob in pmf.Items()])
