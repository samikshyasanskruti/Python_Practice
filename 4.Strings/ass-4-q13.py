def upperword():
    while True:
        w=input(" plz enter upper case ")
        if w.isupper():
            print(" thankyou ")
            break
        else:
            print(" try again ")
def main():
    upperword()
if __name__=="__main__":
    main()
