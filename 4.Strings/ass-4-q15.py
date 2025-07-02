def pig(w):
    vowels="aeiou"
    w=w.lower()
    if w[0] in vowels:
        return w +'way'
    else:
        return w[1:]+w[0]+'ay'
def main():
    n=input(" enter")
    print(pig(n))
if __name__=="__main__":
    main()