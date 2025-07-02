c=input("enter the character ")
n=ord(c)
if (n>=97 and n<=122):
    print(" the character is lower case")
elif (n>=65 and n<=90):
    print(" the character is upper case")
elif (n>=48 and n<=57):
    print(" the character is numeric")
else :
    print(" the character is special case")