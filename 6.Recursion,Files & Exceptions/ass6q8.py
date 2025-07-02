def power_of(value, exponent):
    if exponent == 0:
        return 1
    return value * power_of(value, exponent - 1)
if __name__ == "__main__":
    print(power_of(4, 2))
