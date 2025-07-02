import math
a=float(input("enter the value of a "))
b=float(input("enter the value of b "))
c=float(input("enter the value of c "))
d=b**2-(4*a*c)
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
if(d>0):
    print("two roots ",r1,"  ",r2)
elif(d==0):
    print("one root ",r1,"  ")
else:
    print(" no  real roots ")