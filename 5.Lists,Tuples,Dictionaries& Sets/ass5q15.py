def char_histogram(message):
    freq = {}
    for char in message:
        freq[char] = freq.get(char, 0) + 1
    return freq
if __name__ == "__main__":
    message = input("Enter a message: ")
    histogram = char_histogram(message)
    print("Character Frequency Histogram:")
    for char, count in histogram.items():
        print(f"{char}: {count}")
