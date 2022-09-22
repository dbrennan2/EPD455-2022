# creating sparse matrix
arr = [[1, 0, 0, 18, 0],
       [0, 36, 2, 0, 0],
       [0, 0, 63, 0, 0],
       [0, 0, 0, 10, 0],
       [90, 0, 0, 0, 7]]
 
# creating empty dictionary
dic = {}
 
# iterating through the matrix
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != 0:
            # Insert code here to add non zero elements to the 
            # dictionary "dic"

print("Position of non-zero elements in the matrix:")
print(dic)