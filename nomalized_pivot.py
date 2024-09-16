def normalize_pivot(matrix):
    """Ensure that pivot elements are 1 by dividing rows by their pivot."""
    for i in range(min(len(matrix), len(matrix[0]))):
        if matrix[i][i] != 0:
            pivot = matrix[i][i]
            for j in range(len(matrix[i])):
                matrix[i][j] /= pivot
    return matrix