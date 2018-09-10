import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)
white_wines = np.genfromtxt('winequality-white.csv',delimiter=';',skip_header=1)

all_wines = np.vstack((wines, white_wines))

print(all_wines)

xyz = np.concatenate((wines, white_wines), axis=0)

print(xyz)