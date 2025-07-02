def calc_primes_up_to(max_value):
    primes = []
    for num in range(2, max_value + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes
if __name__ == "__main__":
    print(calc_primes_up_to(30))
