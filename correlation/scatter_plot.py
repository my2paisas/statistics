'''
Scatter plot example
'''
import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.normal(0, 1, N)
y = x - np.random.normal(0, 0.75, N)

# correlation coefficient
print np.corrcoef(x, y)[0, 1]

plt.scatter(x, y)
plt.show()
