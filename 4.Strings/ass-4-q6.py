def word(s):
    result=" "
    for i in range(len(s)):
        char=s[i]
        if i==0 or s[i-1]==' ':
            if 'a' <=char<= 'z':
                result+=chr(ord(char)-32)
            else:
                result+=char
        else:
            if 'A'<=char<='Z':
                result+=chr(ord(char)+32)
            else:
                result+=char
    return result
def main():
    n1=input(" enter the string ")
    print(word(n1))
if __name__=='__main__':
     main()
