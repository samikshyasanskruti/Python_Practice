def calc_checksum(digits):
    total = sum((i + 1) * int(d) for i, d in enumerate(digits))
    return total % 10
if __name__ == "__main__":
    print(calc_checksum("87654321"))
