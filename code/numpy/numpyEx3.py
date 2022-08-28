import numpy as np

A = np.ones((3, 2))
B = np.ones((2, 3))

print(np.dot(A,B))
print(np.dot(B.T,A.T))
print(np.dot(A.T,B.T))

# this will crash, wrong dims
print(np.dot(A.T,B))