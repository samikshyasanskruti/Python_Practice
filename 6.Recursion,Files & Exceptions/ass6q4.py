def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    return abs(a * b) // gcd(a, b)
if __name__ == "__main__":
    print(lcm(4, 6)) 
