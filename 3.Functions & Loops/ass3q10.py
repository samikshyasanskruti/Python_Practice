def is_number_palindrome(number):
    rev = 0
    original = number
    while number > 0:
        rev = rev * 10 + number % 10
        number //= 10
    return rev == original
if __name__ == "__main__":
    print(is_number_palindrome(121))
