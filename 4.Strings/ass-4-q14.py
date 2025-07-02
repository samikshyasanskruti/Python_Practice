def backword():
    word= input ("enter a word ")
    for char in reversed(word):
        print(char,end='')
def main():
    backword()
if __name__=="__main__":
    main()