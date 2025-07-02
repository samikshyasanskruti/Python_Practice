def remove_duplicates(values):
    seen = set()
    result = []
    for val in values:
        if val not in seen:
            result.append(val)
            seen.add(val)
    return result
if __name__ == "__main__":
    lst = list(map(int, input("Enter numbers: ").split()))
    print("Without duplicates:", remove_duplicates(lst))
