def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]
if __name__ == "__main__":
    print("Enter elements for matrix A:")
    a = [list(map(int, input().split())) for _ in range(3)]
    print("Enter elements for matrix B:")
    b = [list(map(int, input().split())) for _ in range(3)]
    result = add_matrices(a, b)
    print("Sum of matrices:")
    for row in result:
        print(row)
