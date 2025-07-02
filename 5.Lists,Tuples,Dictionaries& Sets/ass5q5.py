def column_sums(matrix):
    for col in range(len(matrix[0])):
        col_sum = sum(row[col] for row in matrix)
        print(f"Sum of the elements at column {col} is {col_sum}")
if __name__ == "__main__":
    matrix = []
    print("Enter a 3-by-4 matrix row by row:")
    for _ in range(3):
        matrix.append(list(map(float, input().split())))
    column_sums(matrix)
