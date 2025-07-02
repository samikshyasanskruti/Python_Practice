def repated_char(s):
    r=s[0]
    for i in range (1,len(s)):
        if s[i]==s[i-1]:
            r+='*'
        else:
            r+=s[i]
        return r
def main():
    n= input(" enter a  word ")
    print(repated_char(n))
if __name__=='__main__':
     main()