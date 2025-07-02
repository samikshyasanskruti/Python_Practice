def find_minimum(lst):
    return min(lst)
if __name__ == "__main__":
    nums = list(map(float, input("Enter ten numbers: ").split()))
    print("The minimum number is:", find_minimum(nums))
