"""matrix multiplication"""
import numpy as np

class coloumsandrowmismatchError(Exception):
    pass

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[7,9],[3,4],[4,3]])
a1r=arr1.shape[0]
a1c=arr1.shape[1]
a2r=arr2.shape[0]
a2c=arr2.shape[1]

narr=np.zeros((a1r,a2c))

try:
    if a1c!=a2r:
        raise coloumsandrowmismatchError("the no. of column of the first matrix and the "
                                         "no. of rows of the second matrix does not match ")
    for i in range(a1r):
        for j in range(a2c):
            for k in range(a1c):
                narr[i][j]+=arr1[i][k]*arr2[k][j]
except coloumsandrowmismatchError as e:
    print(e)
else:
    print(narr)