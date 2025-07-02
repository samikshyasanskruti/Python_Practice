n=int (input(" enter todays day "))
d=int(input(" enter no of days elpased since today "))
j=(n+d)//7
print(" todays day is ",end=" ")
if(n==1):
    print("mon")
elif(n==2):
    print("tue")
elif(n==3):
    print("wed")
elif(n==4):
    print("thur")
elif(n==5):
    print("fri")
elif(n==6):
    print("sat")
elif(n==0):
    print("sun")
else:
    print("re enter day ")


if(j==1):
    print("future day is mon")
elif(j==2):
    print("future day is tue")
elif(j==3):
    print("future day is wed")
elif(j==4):
    print("future day is thur")
elif(j==5):
    print("future day is fri")
elif(j==6):
    print("future day is sat")
elif(j==0):
    print("future day is sun")
else:
    print("re enter day ")

