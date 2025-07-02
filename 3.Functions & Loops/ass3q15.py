import math
def exp_taylor(x, terms=10):
    result = 0
    for i in range(terms):
        result += x**i / math.factorial(i)
    return result
if __name__ == "__main__":
    print(exp_taylor(1))
