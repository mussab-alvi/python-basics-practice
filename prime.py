n=int(input("Enter a number to check: "))
for i in range (2,n):
    if(n%i==0):
        print("Number you enter is not a prime. ")
        break
    else:
        print("The number you enter is a prime number. ")
        break