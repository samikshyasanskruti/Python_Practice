def is_magic_triangle(values):
    if len(values) < 6:
        return False
    a = values[0] + values[1] + values[2]
    b = values[2] + values[3] + values[4]
    c = values[4] + values[5] + values[0]
    return a == b == c
if __name__ == "__main__":
    values = list(map(int, input("Enter 6 numbers: ").split()))
    print("Is magic triangle?", is_magic_triangle(values))
