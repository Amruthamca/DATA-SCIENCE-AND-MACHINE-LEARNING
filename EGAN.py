print("Amrutha Biju")
print("21MCA003")

import numpy as np
m = np.random.randint(10, size=(3, 3))
print(m)
print("INVERSE")
inverse=np.linalg.inv(m)
print(inverse)
print("RANK OF MATRIX")
rank = np.linalg.matrix_rank(m)
print(rank)

print("DETERMINANT")
det=np.linalg.det(m)
print(det)
print("transform matrix into 1D")
tmatrix = np.ravel(m)
print(tmatrix)
w, v = np.linalg.eig(m)
print("Printing the Eigen values of the given square matrix:\n",w)
print("Printing Right eigenvectors of the given square matrix:\n",v)

