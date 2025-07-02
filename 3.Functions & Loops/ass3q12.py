def pattern_a(n):
    for i in range(1, n+1):
        print("* " * i)
def pattern_b(n):
    for i in range(1, n+1):
        print(" ".join(str(j) for j in range(1, i+1)))
def pattern_c(n):
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(1, i+1)))
def pattern_d(n):
    for i in range(n, 0, -1):
        print("* " * i)
if __name__ == "__main__":
    pattern_a(5)
    print()
    pattern_b(5)
    print()
    pattern_c(5)
    print()
    pattern_d(5)
