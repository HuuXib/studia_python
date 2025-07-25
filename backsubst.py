import numpy as np


def backsubst(A,b):
    m,n = A.shape
    o = b.size
    x = np.zeros(o)
    assert(m==n and m==o)
    for i in range (n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += A[i,j]*x[j]
            x[i]= (b[i] - sum)/A[i,i]
    return x
