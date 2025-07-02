def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
def calc_friends(max_exclusive):
    friends = []
    for a in range(2, max_exclusive):
        b = sum_of_divisors(a)
        if b != a and b < max_exclusive and sum_of_divisors(b) == a:
            if (b, a) not in friends:
                friends.append((a, b))
    return friends
if __name__ == "__main__":
    print(calc_friends(10000))
