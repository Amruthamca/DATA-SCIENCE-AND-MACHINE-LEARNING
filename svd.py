print("21mca003")
import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
U, D, VT = np.linalg.svd(A)
print("Decomposed value of U :")
print(U)
print()
print("Decomposed value of D :")
print(D)
print()
print("Decomposed value of VT :")
print(VT)
print()
A_remake = (U @ np.diag(D) @ VT)
print("The SVD of a given matrix. :")
print(A_remake)

