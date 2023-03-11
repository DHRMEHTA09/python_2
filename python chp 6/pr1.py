a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
max=0
if(a>=b and a>=c and a>=d):
    max=a
elif(b>=a and b>=c and b>=d):
    max=b
elif(c>=a and c>=b and c>=d):
    max=c
else:
    max=d
print("the greatesr value is: ",max)                