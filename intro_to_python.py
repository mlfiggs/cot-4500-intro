import numpy as np
matrix = np.eye(3)
print(matrix)

matrix[matrix != 1] += 3
print(matrix)

matrix = np.delete(matrix, -1, 1)
print(matrix)