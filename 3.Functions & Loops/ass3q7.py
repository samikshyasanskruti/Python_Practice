def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
if __name__ == "__main__":
    print([i for i in range(1, 501) if is_perfect(i)])
