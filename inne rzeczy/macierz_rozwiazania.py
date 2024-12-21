import numpy as np
from sympy import Matrix

# Define the coefficient matrix A and result vector B
A = np.array([
    [1, 2, 3, -2],
    [3, 6, 5, -4],
    [1, 2, 7, -4],
    [2, 4, 2, -3]
], dtype=float)

B = np.array([4, 5, 11, 6], dtype=float)

# Create the augmented matrix
A_extended = np.column_stack((A, B))

# Calculate the rank of A and the augmented matrix
rank_A = np.linalg.matrix_rank(A)
rank_A_extended = np.linalg.matrix_rank(A_extended)

print("Rank of A:", rank_A)
print("Rank of the augmented matrix:", rank_A_extended)

# Check the system's consistency
if rank_A == rank_A_extended:
    print("The system is consistent.")
    if rank_A < A.shape[1]:
        print("The system has infinitely many solutions.")
    else:
        print("The system has a unique solution.")
else:
    print("The system is inconsistent.")

# Solve the system using row-reduced echelon form
augmented_matrix = Matrix(A_extended).rref()
print("\nRow-reduced echelon form of the augmented matrix:")
print(augmented_matrix[0])

# Interpret free variables and general solutions
