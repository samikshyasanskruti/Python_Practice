a=float(input("enter the value of a "))
b=float(input("enter the value of b "))
c=float(input("enter the value of c "))
d=float(input("enter the value of d "))
e=float(input("enter the value of e "))
f=float(input("enter the value of f "))
check =(a*d)-(b*c)
if check ==0:
    print(" no solution ")
else :
   x=(e*d-b*f)/(a*d-b*c)
   y=(a*f-e*c)/(a*d-b*c)
   print("x: ",x," y: ",y)