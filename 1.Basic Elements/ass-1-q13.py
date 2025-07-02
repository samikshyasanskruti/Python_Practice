n =int(input('input a 4 digit number'))
w=n//1000
x=(n//100)%10
y=(n//10)%10
z=n%10
sum=w+x+y+z
print("sum of 4 digit number is : ",sum)