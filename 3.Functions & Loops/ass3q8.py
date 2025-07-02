def to_binary(n):
    result = ""
    if n == 0: return "0"
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result
if __name__ == "__main__":
    print(to_binary(42))
