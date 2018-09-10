import numpy as np

wines = np.genfromtxt('winequality-red.csv', delimiter=';', skip_header=1)

print(wines[:,11] > 5)
print((wines[:,11] > 5).dtype)