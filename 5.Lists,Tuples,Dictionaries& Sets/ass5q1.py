import random
def list_operations(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    total = sum(lst)
    average = total / n
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return lst, total, average, even, odd
if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    lst, total, average, even, odd = list_operations(n)
    print("List:", lst)
    print("Sum:", total)
    print("Average:", average)
    print("Even values:", even)
    print("Odd values:", odd)
