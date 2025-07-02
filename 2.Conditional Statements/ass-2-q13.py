import random
n=int ( input("scissoors(0)    rocks(1)   paper(2)  enter your choice  "))
c= random.randint(0,2)
print(" coomputer choice is ",c)
if(n==0 and c==1):
    print(" you lost ")
elif(n==0 and c==2):
    print(" you  won ")
elif(n==c):
    print(" draw ")
elif(n==1 and c==2):
    print(" you lost ")
elif(n==1 and c==0):
    print(" you won ")
elif(n==2 and c==0):
    print(" you lost ")
else:
    print(" ypu won ")




