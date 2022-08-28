import numpy as np

A = np.array([[1,4,3],
    [5,2,7]])

print(A)
print("Sum:", A.sum())
print("Sum, along axis 0:", A.sum(axis=0))
print("Sum, along axis 1:", A.sum(axis=1))
print("Prefix scan:", A.cumsum())
print("Prefix scan, down the row:", A.cumsum(axis=0))
print("Prefix scan, down the column:", A.cumsum(axis=1))

print("Min, amongst the rows:", A.min(axis=0))
print("Max, amongst the columns:", A.max(axis=1))