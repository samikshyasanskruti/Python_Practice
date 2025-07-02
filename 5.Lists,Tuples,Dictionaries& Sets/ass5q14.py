def fibonacci_dict(n):
    fib = {0: 0, 1: 1}
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print(f"{n}th Fibonacci number is:", fibonacci_dict(n))
