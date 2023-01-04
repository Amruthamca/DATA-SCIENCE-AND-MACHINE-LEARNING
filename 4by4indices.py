print("Amrutha Biju")
print("21MCA003")
import numpy as np
X = np.array( [ [ 1, 6, 7, 4],
[ 5, 9, 2, 1],
[ 3, 8, 4, 6],
[ 2, 3, 6, 1] ] )
print("Original form")
print(X)
print("Excluding the first row")
print(X[1:,])
print("Alternate method for Excluding the first row")
num=np.delete(X,0,axis=0)
print(num)
print("Excluding last column")
print(X[:, :-1])
print("Display the elements of 1st and 2nd column in 2nd and 3rd row")
print(X[1:3,0:2])
print("Display the elements of 2nd and 3rd column")
print(X[:,[1,2]])
print("Display 2nd and 3rd element of 1st row")
print(X[0:1,1:3])
print("Display the elements from indices 4 to 10 in descending order")
flat_array=X.flatten()
print(flat_array)
new=sorted(flat_array[-3:-10])
index=flat_array[11:4:-1]
print(index)

