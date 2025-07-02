x=int(input("enter x coordinate "))
y=int(input("enter y coordinate "))

if(x==0 and y==0):
    print("( ",x," , ",y," ) is in origin")
elif(x==0 and y!=0):
    print("( ",x," , ",y," ) is in y axis")
elif(x!=0 and y==0):
    print("( ",x," , ",y," ) is in x axis")
elif(x>0 and y>0):
    print("( ",x," , ",y," ) is in 1 quadrant ")
elif(x<0 and y<0):
    print("( ",x," , ",y," ) is in 4 quadrant ")
elif(x<0 and y>0):
    print("( ",x," , ",y," ) is in 2 quadrant ")
else:
    print("( ",x," , ",y," ) is in 3 quadrant ")