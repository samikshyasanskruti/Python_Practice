w= float(input("enter weignt in kg"))
h=float(input(" eneter height in meters"))
a=w/(h**2)
if(a<18.5):
    print(" you are under weight  ")
elif(18.5<a and a<24.9):
    print(" you are normal weight  ")
elif(25<a and a<29.9):
    print(" you are  over weight  ")
else:
    print(" you are obese  ")

