import numpy as np

A = np.array([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]])

B = np.array([[2, 2, 2],
              [2, 2, 2],
              [2, 2, 2]])

print(np.column_stack((A,B)))
print(np.row_stack((B,A,B)))
