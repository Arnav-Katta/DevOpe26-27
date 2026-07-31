def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Matrix dimensions are incompatible for multiplication")

    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            total = 0
            for k in range(len(matrix_b)):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    print(multiply_matrices(A, B))
