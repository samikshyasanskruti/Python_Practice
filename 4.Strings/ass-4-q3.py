def rearrangement(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
def main():
    n1=input(" enter the string1 ")
    n2=input(" enter the string2 ")
    print(rearrangement(n1,n2))
if __name__=='__main__':
     main()