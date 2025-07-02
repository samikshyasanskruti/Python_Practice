def to_octal(n):
    if n == 0:
        return ''
    return to_octal(n // 8) + str(n % 8)
def to_hex(n):
    hex_chars = '0123456789ABCDEF'
    if n == 0:
        return ''
    return to_hex(n // 16) + hex_chars[n % 16]
if __name__ == "__main__":
    print(to_octal(100))  
    print(to_hex(255))   
