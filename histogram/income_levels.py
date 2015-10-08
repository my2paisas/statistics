'''
Plot a histogram
Statistics, Freedman et al. 3/e
p 35 Table 1
'''
from __future__ import division
from random import randint
import matplotlib.pyplot as plt

# number of sample points for the histogram
sample_size = 100000

# last row changed to assume max income of 60000
# endpoint convention: left included, right excluded
low_high_percents = [(0, 1000, 1),
                     (1000, 2000, 2),
                     (2000, 3000, 3),
                     (3000, 4000, 4),
                     (4000, 5000, 5),
                     (5000, 6000, 5),
                     (6000, 7000, 5),
                     (7000, 10000, 15),
                     (10000, 15000, 26),
                     (15000, 25000, 26),
                     (25000, 50000, 8),
                     (50000, 60000, 1)
                    ]

# create a new list with ranges represented by as much
# frequency as the percents
weighted_ranges = []
for low, high, percent in low_high_percents:
    for i in xrange(0, percent):
        weighted_ranges.append((low, high))

# generate random salaries according to the percents
random_salaries = []
for i in xrange(0, sample_size):
    # randint(a, b) gives a random integer in the closed interval [a, b] 
    random_index = randint(0, len(weighted_ranges) - 1)
    random_range = weighted_ranges[random_index]
    low, high = random_range[0], random_range[1]
    # endpoint convention is to include low, but not high
    random_salary = randint(low, high - 1)
    # count in thousands for ease of plot in histogram
    random_salaries.append(random_salary / 1000)

# plot the histogram; normed=True makes y-axis as probability
plt.hist(random_salaries, bins=[low / 1000 for low, high, percent in low_high_percents], normed=True)
plt.title("Income Levels")
plt.xlabel("Income (in thousands of dollars)")
plt.ylabel("Probability per thousand dollars")
plt.show()
