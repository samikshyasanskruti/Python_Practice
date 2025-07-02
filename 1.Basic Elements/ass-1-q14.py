a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
s=min(a,b,c)
l=max(a,b,c)
m=a+b+c-s-l
print("sorted order is ",s,m,l)