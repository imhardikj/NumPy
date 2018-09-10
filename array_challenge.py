import  numpy as np

array_1 = np.zeros((3,4))
array_2 = np.zeros((6,4))

array_2[:, :] = 1

array = np.vstack((array_1, array_2))

first_column = array[:, 1]

print(first_column)