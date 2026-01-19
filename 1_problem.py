a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter forth number: "))
if(a>b and a>c and a>d ):
    print(a, "is greater then", b,"-" , c,"-" ,d)
elif(b>a and b>c and b>d ):
    print(b, "is greater then", a,"-" , c,"-" ,d)
elif(c>b and c>a and c>d ):
    print(c, "is greater then", a,"-" , b,"-" ,d)
elif(d>b and d>c and d>a ):
    print(d, "is greater then", a,"-" , b,"-" ,c)
