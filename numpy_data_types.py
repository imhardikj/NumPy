import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)
print(wines.dtype)

int_wines = wines.astype(int)

print(int_wines.dtype.name)

int_wines = wines.astype(np.int64)

print(int_wines.dtype.name)