post="Artificial Intelligence (AI) is transforming cybersecurity" 
"by making threat detection, prevention, and response faster and more accurate."
a=input("Enter word you want to search: ")
if (a.lower() in post.lower()):
    print (a, "is present in this post !!!")
else:
    print(a,"is not present in this post ")


print ("Have a nice day :)")