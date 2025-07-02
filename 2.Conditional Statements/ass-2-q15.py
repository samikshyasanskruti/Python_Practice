g= input (" enter your gender m/f").upper()
n1= input(" enter first name ")
n2= input(" enter last  name ")
a= int (input (" enter the age "))
if(g=='F'):
    if(a>=10):
        s=(" are you married y/n ").upper()
        if(s=='y'):
            print(" i shall call you mrs ",n1,n2)
        else:
            print(" i shall call you ms",n1,n2)
elif(g=='M'):
    if(a>=20):
        print(" i shall call you mr",n1,n2)
elif(g=='F'):
    if(a<10):
        print(" i shall call you ",n1,n2)
else:
    print(" i shall call you  ",n1,n2)