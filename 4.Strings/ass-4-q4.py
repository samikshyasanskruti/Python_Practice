def replacement(s):
    s=s.replace(" ","")
    c1=0

    for i in range(0,len(s)):
        
        c=0
        for j in range(i,len(s)):
            if(s[i]==s[j]):
                c+=1
        if c>c1:
            c1=c
            k=s[i]

    s=s.replace(k,'-')
    return s
def main():
    n1=input(" enter the string ")
    print(replacement(n1))
if __name__=='__main__':
     main()