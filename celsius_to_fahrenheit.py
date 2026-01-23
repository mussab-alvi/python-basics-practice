def f_to_c(f):
    return 5/9*(f-32)
   
p=int(input("Enter tempreture in fahrenheit: "))

print (f"{round(f_to_c (p),2)}°C")