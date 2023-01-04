print("Amrutha Biju")
print("21mca003")
import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
b = np.array([[-3],
              [5],
              [-2]])
a=np.linalg.inv(A)
x= np.linalg.solve(a, b)
print("Value of X=A -1 b: ")
print(x)
