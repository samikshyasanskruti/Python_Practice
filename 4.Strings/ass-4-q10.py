def rep(s):
    first=s[0]
    modified=first+s[1:].replace(first,'$')
    return modified
def main():
  n=input("enter a string ")
  print(rep(n))

if __name__=="__main__":
    main()
                                 