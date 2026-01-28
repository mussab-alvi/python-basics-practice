def remove(m,specific):
    s=[]
    for item in m:
       if not (item ==specific):
           s.append(item.strip(specific))
    return s

m = ["Mussab", "Hassan", "Sami", "mi"]

print(remove(m,"mi"))


