print("REVERSE AN ARRAY")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

a.reverse()   
print(a)
