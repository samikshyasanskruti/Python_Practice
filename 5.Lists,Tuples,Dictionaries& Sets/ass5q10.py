def mergeList(values1, values2):
    result = []
    i = j = 0
    while i < len(values1) and j < len(values2):
        if values1[i] < values2[j]:
            result.append(values1[i])
            i += 1
        else:
            result.append(values2[j])
            j += 1
    result += values1[i:] + values2[j:]
    return result
if __name__ == "__main__":
    list1 = list(map(int, input("Enter sorted list 1: ").split()))
    list2 = list(map(int, input("Enter sorted list 2: ").split()))
    print("Merged list:", mergeList(list1, list2))
