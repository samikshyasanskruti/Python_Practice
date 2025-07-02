n=int (input(" enter a number "))
a='false'
b='false'
d ='false'
if(n%5==0 and n%6==0):
    a='true'
if(n%5==0 or n%6==0):
    b='true'
if((n%5==0 and n%6!=0 ) or( n%5==0 and n%6==0)):
    d ='true'
print("is ",n," divisible by 5 and 6 ? ",a)
print("is ",n," divisible by 5 or 6 ? ",b)
print("is ",n," divisible by 5 or 6 but not by both ? ",d)