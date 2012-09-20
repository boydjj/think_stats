"""
Think Stats Exercise 1-3.

Evaluate the total number of pregnancies, live births, first births, other
births, etc., in the given dataset.
"""

import survey
import sys

def _get_live_births(table):
    lb_sum = 0
    for preg in table.records:
        if preg.outcome == 1:
            lb_sum += 1
    return lb_sum

def partition_births(table):
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()
    
    for preg in table.records:
        if preg.outcome == 1:
            if preg.birthord == 1:
                firsts.AddRecord(preg)
            else:
                others.AddRecord(preg)

    return firsts, others

def _get_avg_preg_length(table):
    total_length = 0
    for preg in table.records:
        total_length += preg.prglength
    return float(total_length) / len(table.records)    
    

if __name__ == '__main__':
    data_dir = sys.argv[1]
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print 'Number of pregnancies:', len(table.records)
    print 'Number of live births:', _get_live_births(table)
    
    firsts, others = partition_births(table)
    print 'Number of first births:', len(firsts.records)
    print 'Number of other births:', len(others.records)
    
    avg_preg_length_firsts = _get_avg_preg_length(firsts)
    avg_preg_length_others = _get_avg_preg_length(others)
    print 'Avg length of first births:', avg_preg_length_firsts
    print 'Avg length of other births:', avg_preg_length_others
    
    diff = avg_preg_length_firsts - avg_preg_length_others
    print 'Difference:', diff , 'weeks (' + str(diff * 7 * 24) + ' hours)'