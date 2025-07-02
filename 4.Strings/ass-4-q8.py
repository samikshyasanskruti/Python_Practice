def separate(word):
    vowels="aeiouAEIOU"
    result=list()
    temp=""
    for char in word:
        if char in vowels:
            if temp:
                result.append(temp)
                temp=""
        else:
            temp+=char
    if temp:
        result.append(temp)
    return result
def main ():
    n1=input(" enter the string ")
    print(separate(n1))
if __name__=='__main__':
     main()