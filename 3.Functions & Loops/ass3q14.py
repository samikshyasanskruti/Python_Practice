import math
def sin_taylor(x, terms=10):
    result = 0
    for i in range(terms):
        sign = (-1)**i
        result += sign * (x**(2*i+1)) / math.factorial(2*i+1)
    return result
def cos_taylor(x, terms=10):
    result = 0
    for i in range(terms):
        sign = (-1)**i
        result += sign * (x**(2*i)) / math.factorial(2*i)
    return result
if __name__ == "__main__":
    x = math.pi / 4
    print("sin(x):", sin_taylor(x))
    print("cos(x):", cos_taylor(x))
