import numpy as np

wines = np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)
high_quality = wines[:,11] > 7
print(wines[high_quality,:][:3,])


high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)

print(wines[high_quality_and_alcohol,10:])
