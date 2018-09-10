import numpy as np

wines = np.genfromtxt('winequality-red.csv', delimiter=';', skip_header=1)
print(wines[:,11].sum())

print(wines.sum(axis=0))

print(wines.sum(axis=1))
