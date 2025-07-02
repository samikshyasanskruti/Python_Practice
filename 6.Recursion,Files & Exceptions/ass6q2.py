def calc_sum_of_digits(value):
    if value == 0:
        return 0
    return value % 10 + calc_sum_of_digits(value // 10)
if __name__ == "__main__":
    print(calc_sum_of_digits(12345))
