m=int (input(" enter the month "))
y=int (input(" enter the  year "))
assert (m>=1)or(m<=12)," imvalid month !!"
assert (y>=1582)," no record found !!"
if((y%100==0 or y%4==0 )and m==2):
    n=29
elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 ):
    n=31
else:
    n=30

if(m==1):
    print("jan", end=" ")
elif(m==2):
    print("feb", end=" ")
elif(m==3):
    print("march", end=" ")
elif(m==4):
    print("april", end=" ")
elif(m==5):
    print("may", end=" ")
elif(m==6):
    print("june", end=" ")
elif(m==7):
    print("july", end=" ")
elif(m==8):
    print("aug", end=" ")
elif(m==9):
    print("sept", end=" ")
elif(m==10):
    print("oct", end=" ")
elif(m==11):
    print("nov", end=" ")
elif(m==12):
    print("dec", end=" ")
else:
    print("re enter invalid month ")
print (" ",y," had ",n," days")