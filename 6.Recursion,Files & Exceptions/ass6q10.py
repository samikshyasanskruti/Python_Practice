def harmonic_sum(n):
    if n == 1:
        return 1
    return 1 / n + harmonic_sum(n - 1)
if __name__ == "__main__":
    print(harmonic_sum(4)) 
