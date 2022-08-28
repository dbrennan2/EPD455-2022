import numpy as np

#2D array of integers
u = np.array([1, 2, 3])
v = np.array([1, 1, 1])

# inner product
print(np.inner(u,v))

# outer product
print(np.outer(u,v))

# dot product
print(np.dot(u,v))