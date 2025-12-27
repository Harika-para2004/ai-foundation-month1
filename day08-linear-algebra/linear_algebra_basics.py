# vectors
import numpy as np

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    return res

def vector_addition(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    res = []
    for i in range(len(v1)):
        res.append(v1[i] + v2[i])
    return res

def scalar_multiplication(scalar, v):
    res = []
    for i in range(len(v)):
        res.append(scalar * v[i])
    return res

# matrices
def matrix_addition(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Matrices must be of the same dimensions")
    res = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        res.append(row)
    return res

def matrix_multiplication(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
    res = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            sum_product = 0
            for k in range(len(m1[0])):
                sum_product += m1[i][k] * m2[k][j]
            row.append(sum_product)
        res.append(row)
    return res

def transpose_matrix(m):
    res = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        res.append(row)
    return res

def determinant_2x2(m):
    if len(m) != 2 or len(m[0]) != 2:
        raise ValueError("Matrix must be 2x2")
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def determinant_3x3(m):
    if len(m) != 3 or len(m[0]) != 3:
        raise ValueError("Matrix must be 3x3")
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
            m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
            m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
# Example usage
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Dot Product:", dot_product(v1, v2))
    print("Vector Addition:", vector_addition(v1, v2))
    print("Scalar Multiplication:", scalar_multiplication(2, v1))

    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print("Matrix Addition:", matrix_addition(m1, m2))
    print("Matrix Multiplication:", matrix_multiplication(m1, m2))
    print("Transpose of Matrix m1:", transpose_matrix(m1))
    print("Determinant of 2x2 Matrix m1:", determinant_2x2(m1))

    m3 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    print("Determinant of 3x3 Matrix m3:", determinant_3x3(m3))


# Note: For larger matrices and more complex operations, consider using NumPy for efficiency and simplicity.
# Now by using numpy
def numpy_matrix_operations():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("NumPy Matrix Addition:\n", a + b)
    print("NumPy Matrix Multiplication:\n", np.dot(a, b))
    print("NumPy Transpose of Matrix a:\n", a.T)
    print("NumPy Determinant of Matrix a:", np.linalg.det(a))

numpy_matrix_operations()    