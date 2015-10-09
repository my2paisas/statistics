'''
Provides methods for
Averages: mean, median, mode
Spreads: standard deviation, inter-quartile range
Pearson correlation coefficient
'''

import numpy as np

def mean(lst):
    if len(lst) == 0:
        return None
    return np.mean(lst)

def median(lst):
    if len(lst) == 0:
        return None
    return np.median(lst)

def mode(lst):
    if len(lst) == 0:
        return None
    return max(set(lst), key=lst.count)

def std(lst):
    '''standard deviation'''
    if len(lst) == 0:
        return None
    return np.std(lst)

def iqr(lst):
    '''inter-quartile range'''
    if len(lst) == 0:
        return None
    q1, q3 = np.percentile(lst, [25, 75])
    return q3 - q1

if __name__ == '__main__':
    lst = [0, 0, 0, 1, 1, 100, 500, 1000]
    print('  list = {}'.format(lst))
    print('  mean = {}'.format(mean(lst)))
    print('median = {}'.format(median(lst)))
    print('  mode = {}'.format(mode(lst)))
    print('stddev = {}'.format(std(lst)))
    print('   iqr = {}'.format(iqr(lst)))
