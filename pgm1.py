import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[2,4,6],[1,3,5],[11,12,13]])
print("MATRIX x \n",x)
print("MATRIX y \n",y)

a=7*x
b=np.power(y,3)
print("the operation of 7X+y^3")
result=a+b
print(result)

print("matrix multiplication of x and y")
c = np.matmul(x,y)
print(c)

print("Diagonal element of matrix x")
c1 = np.diagonal(x)
print(c1)

print("Diagonal element of matrix y")
c2 = np.diagonal(y)
print(c2)

print("Rank of matrix x ")
print(np.linalg.matrix_rank(x))

print("Rank of matrix y ")
print(np.linalg.matrix_rank(y))










