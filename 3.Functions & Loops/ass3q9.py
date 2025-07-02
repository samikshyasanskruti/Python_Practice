def to_octal(n):
    result = ""
    if n == 0: return "0"
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result
def to_hex(n):
    hex_chars = "0123456789ABCDEF"
    result = ""
    if n == 0: return "0"
    while n > 0:
        result = hex_chars[n % 16] + result
        n //= 16
    return result
if __name__ == "__main__":
    print(to_octal(42))
    print(to_hex(77))
