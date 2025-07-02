def is_number_palindrome(number):
    def helper(n, rev):
        if n == 0:
            return rev
        return helper(n // 10, rev * 10 + n % 10)
    return number == helper(number, 0)
if __name__ == "__main__":
    print(is_number_palindrome(121))  
    print(is_number_palindrome(123))
