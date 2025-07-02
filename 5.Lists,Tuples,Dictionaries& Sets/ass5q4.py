def eliminate_duplicates(lst):
    return list(set(lst))
if __name__ == "__main__":
    nums = list(map(int, input("Enter ten numbers: ").split()))
    print("The distinct numbers are:", *eliminate_duplicates(nums))
