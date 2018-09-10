import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)
print(wines)

print(wines[2, 3])

print(wines[0:3, 3])

print(wines[1, 5])
wines[1, 5] = 10
print(wines[1, 5])

print(wines[:, 5])
wines[:, 5] = 50
print(wines[:, 5])

third_wine = wines[3, :]              # 1-D array
print(third_wine[2])
