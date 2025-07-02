def calc_armstrong_numbers():
    result = []
    for num in range(100, 1000):
        x = num // 100
        y = (num // 10) % 10
        z = num % 10
        if x**3 + y**3 + z**3 == num:
            result.append(num)
    return result
if __name__ == "__main__":
    print(calc_armstrong_numbers())
