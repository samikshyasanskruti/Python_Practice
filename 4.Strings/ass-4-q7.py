def oddeven(s):
    words=s.split()
    odd=0
    even=0
    for word in words:
        if len(word)%2==0:
            even+=1
        else:
            odd+=1
    return odd,even
def main():
    n1=input(" enter the string ")
    oddcount,evencount=oddeven(n1)

    print("odd count = ",oddcount)
    print("evev count = ",evencount)

if __name__=='__main__':
     main()


