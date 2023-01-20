# import the numpy library
import numpy as np

# create an identity vector
matrix = np.eye(3)
print(matrix)

# replace all non-ones with three
matrix[matrix != 1] += 3
print(matrix)

# remove the last column in the matrix
matrix = np.delete(matrix, -1, 1)
print(matrix)