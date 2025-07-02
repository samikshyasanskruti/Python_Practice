def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
if __name__ == "__main__":
    print("GCD of 42 and 28:", gcd(42, 28))
    print("LCM of 42 and 28:", lcm(42, 28))
