def multiply_matrices(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in
 range(3)]
if __name__ == "__main__":
    print("Enter elements for matrix A:")
    a = [list(map(int, input().split())) for _ in range(3)]
    print("Enter elements for matrix B:")
    b = [list(map(int, input().split())) for _ in range(3)]
    result = multiply_matrices(a, b)
    print("Product of matrices:")
    for row in result:
        print(row)
