def reverse_string(text):
    if len(text) == 0:
        return text
    return text[-1] + reverse_string(text[:-1])
if __name__ == "__main__":
    print(reverse_string("hello")) 
