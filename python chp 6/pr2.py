m1=float(input("enter your maths marks: "))
m2=float(input("enter your physics marks: "))
m3=float(input("enter your chemistry marks: "))
m=(m1+m2+m3)/3.0
if(m1>33.0 and m2>33.0 and m3>33.0 and m>40):
    print("pass")
else:
    print("fail")    