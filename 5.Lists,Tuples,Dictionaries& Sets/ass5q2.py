from collections import Counter
def count_occurrences(lst):
    counter = Counter(lst)
    for num in sorted(counter):
        word = "times" if counter[num] > 1 else "time"
        print(f"{num} occurs {counter[num]} {word}")
if __name__ == "__main__":
    lst = list(map(int, input("Enter integers between 1 and 100 separated by space:").split()))
    count_occurrences(lst)
