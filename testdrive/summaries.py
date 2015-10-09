'''
Test drive for averages
'''
import summary_statistics as ss
from random import gauss

print ss.mean([12, 1, 2])

gaussian_samples = []
for i in xrange(100):
    gaussian_samples.append(gauss(0, 1))
print('Gaussian mean = {}'.format(ss.mean(gaussian_samples)))
print('Gaussian stddev = {}'.format(ss.std(gaussian_samples)))
