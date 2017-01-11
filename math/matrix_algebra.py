# Matrix Algebra
import numpy as np
A =np.array( [[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

##shapes of matrices and array

#1.1) 3x3
print("1.1",A.shape)
#1.2) 2x2
print('1.2',B.shape)
#1.3) 3x2
print('1.3',C.shape)
#1.4) 2x3
print('1.4',D.shape)
#1.5) 1x4
print('1.5',v.shape)
#1.6) 4x1
print('1.6',w.shape)

#2.1) u +v
print(u + v)
#2.2) u-v
print(u-v)
#2.3)alpha * u
print(6*u)
#2.4)u*v
print(u*v)
#2.5) sum(u*u)**1/2
print(sum(u*u)**1/2)

#3.1) A + C
print(A+C)

##undefined. 

#3.2) A -C.T

''' output
array([[-4, -7, -3],
      [ 3,  6,  4]]) '''

#3.3) C.T + 3*D
''' >>> C.T + 3*D
    array([[14,  3,  3],
      [ 2,  7,  9]])'''
#3.4) BA
'''
>>> np.matmul(B,A)
array([[-1, -5, -1],
       [ 2,  7,  4]] '''
#3.5) B*A.T
#undefined


