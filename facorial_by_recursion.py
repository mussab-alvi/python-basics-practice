def fact(n):
    if (n==1 or n==0):
        return 1 
    return n*fact(n-1)

a=int(input("Enter a number: "))
print(f"The factroial of the number is:  {fact(a)}")  
  