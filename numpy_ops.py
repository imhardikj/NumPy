import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)

print(wines[:,11] + 10)          # doesn't modify array

wines[:,11] += 10                # modify's array
print(wines[:,11])

print(wines[:,11]*2)

print(wines[:,10] + wines[:,11])