import random
def generate_matrix():
    matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
    return matrix
def find_largest(matrix):
    row_index = max(range(4), key=lambda i: sum(matrix[i]))
    col_index = max(range(4), key=lambda i: sum(matrix[j][i] for j in range(4)))
    return row_index, col_index
if __name__ == "__main__":
    matrix = generate_matrix()
    for row in matrix:
        print(*row)
    r, c = find_largest(matrix)
    print("The largest row index:", r)
    print("The largest column index:", c)
