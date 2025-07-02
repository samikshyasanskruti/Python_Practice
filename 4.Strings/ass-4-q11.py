def x(sentence,old, new):
    return sentence.replace(old,new)
def main():
  n=input("enter a sentence ")
  old=input("enter word to be replaced ")
  new=input("enter replacement word")
  print(x(n,old,new))

if __name__=="__main__":
    main()