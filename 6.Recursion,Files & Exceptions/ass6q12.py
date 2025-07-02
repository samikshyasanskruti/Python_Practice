def count_words_vowels(file):
    with open(file, 'r') as f:
        text = f.read()
    words = text.split()
    vowels = sum(1 for char in text if char.lower() in 'aeiou')
    print(f"Words: {len(words)}, Vowels: {vowels}")
if __name__ == "__main__":
    count_words_vowels('input.txt')
# use own text file
