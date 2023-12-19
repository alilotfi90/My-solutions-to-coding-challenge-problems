import math

def smallest_power_of_2(n):
    k = math.ceil(math.log2(n))
    return 2**k

def augment_matrix(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])

    n = max(smallest_power_of_2(num_row), smallest_power_of_2(num_col))
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(num_row):
        for j in range(num_col):
            new_matrix[i][j] = matrix[i][j]

    return new_matrix

def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2

    A11 = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]

    return A11, A12, A21, A22

def combine_matrix(A11, A12, A21, A22):
    n = len(A11)
    combined = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

    for i in range(n):
        for j in range(n):
            combined[i][j] = A11[i][j]
            combined[i][j + n] = A12[i][j]
            combined[i + n][j] = A21[i][j]
            combined[i + n][j + n] = A22[i][j]

    return combined

def add_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    return result

def subtract_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]

    return result

def strassen_matrix_multiply(A, B):
    n = len(A)

    if n <= 32:  # Base case, use regular matrix multiplication
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    # Split matrices into quarters
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursive steps
    M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Combine results
    C11 = subtract_matrices(add_matrices(add_matrices(M1, M4), M7), M5)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(M1, M2), M3), M6)

    # Combine submatrices to get the final result
    return combine_matrix(C11, C12, C21, C22)

# Example usage:
A = [[1, 0], [0, 1]]
B = [[1, 0], [0, 1]]


def read_matrix(n):

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Read input matrices A and B
n = int(input())
A = read_matrix(n)
B = read_matrix(n)

# Check if n is a power of 2, if not, augment matrices
if n & (n - 1) != 0:
    n = smallest_power_of_2(n)
    A = augment_matrix(A)
    B = augment_matrix(B)

# Perform matrix multiplication
result = strassen_matrix_multiply(A, B)

print(result)