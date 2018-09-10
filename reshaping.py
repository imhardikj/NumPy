import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)

print(np.transpose(wines))

print(wines.ravel())

print(wines[1, :].reshape((2,6)))
