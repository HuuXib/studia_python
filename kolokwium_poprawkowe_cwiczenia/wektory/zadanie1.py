import numpy as np
import json 

N = int(input('podaj wielkosc macierzy kwadratowej: '))
matrix = np.zeros((N,N))

i = 0
# for w in range(N):
#     for k in range(N):
#         if w >= k:
#             i += 1
#             matrix[w,k] = i



for w in range(N):
     for k in range(N):
            i+=1
            matrix[w,k] = i
            if k == N - w - 1:
                  break
print(matrix)