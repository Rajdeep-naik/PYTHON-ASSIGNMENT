"""Assignment 4: Matrix addition using nested Python lists and NumPy arrays."""

import numpy as np


def add_matrices_using_list(mat_a, mat_b):
    """Performs element-wise matrix addition using nested lists and loops."""
    rows = len(mat_a)
    cols = len(mat_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat_a[i][j] + mat_b[i][j]
    return result


def add_matrices_using_numpy(mat_a, mat_b):
    """Performs element-wise matrix addition using NumPy arrays."""
    np_a = np.array(mat_a)
    np_b = np.array(mat_b)
    return np_a + np_b


def main():
    print(f'{"=" * 45}')
    print(f"{'MATRIX ADDITION':^45}")
    print(f'{"=" * 45}')

    # Take both matrices as input from user
    matrix_a = eval(input("Enter First Matrix: "))
    matrix_b = eval(input("Enter Second Matrix: "))

    # Check if both matrices have the same dimensions
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        print(f"\nError: Cannot add shapes ({rows_a}, {cols_a}) and ({rows_b}, {cols_b}).")
        print("Both matrices must have identical rows and columns!")
    else:
        # Display entered matrices
        print("\nMatrix A:")
        for row in matrix_a:
            print(row)

        print("\nMatrix B:")
        for row in matrix_b:
            print(row)

        # 1. Addition using List
        list_result = add_matrices_using_list(matrix_a, matrix_b)
        print("\n1. Addition using Python List:")
        for row in list_result:
            print(row)

        # 2. Addition using NumPy
        numpy_result = add_matrices_using_numpy(matrix_a, matrix_b)
        print("\n2. Addition using NumPy:")
        print(numpy_result)


if __name__ == "__main__":
    main()