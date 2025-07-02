def x(s):
    c=0
    for i in range(0,len(s)):
        if(s[i]==' '):
            c+=1
    return c+1
def main():
     n1=input(" enter the string ")
     print(x(n1))
if __name__=='__main__':
     main()
