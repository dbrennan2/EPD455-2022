import numpy as np

A = np.array([[1, 4, 3, 0],
              [5, 2, 7, 3],
              [6, 9, 8, 2]])

print(A)
for i in A:
    print(i) # prints a row

for i in A.flat:
    print(i) # prints the entries

for i in A.T.flat:
    print(i) # prints the entries