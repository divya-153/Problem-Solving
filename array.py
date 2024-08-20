# 1)REVERSE AN ARRAY

print("REVERSE AN ARRAY")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

a.reverse()   
print(a)

# 2) FIND MAXIMUM ELEMENT:

print("FIND MAXIMUM ELEMENT:")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
    
print(max(a))

# 3)CALCULATE SUM OF ELEMENTS:

print("3)CALCULATE SUM OF ELEMENTS")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

print(sum(a))

# 4)COUNT OCCURENCES OF AN ELEMENT

print("4)COUNT OCCURENCES OF AN ELEMENT")

from collections import Counter
a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
n=int(input("Enter :"))
c=Counter(a)

for key in c:
    if key==n:
        print(key, ":" , c[key])

# 5) CHECK IF SORTED IN ASCENDING ORDER:

print("5) CHECK IF SORTED IN ASCENDING ORDER:")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
b=sorted(a)
if b==a:
    print("True")
else:
    print("False")

# 6)ROTATE AN ARRAY BY K STEPS:
# a=[1,2,3,4,5] ==> k=2 [4,5,1,2,3]

print("6)ROTATE AN ARRAY BY K STEPS:")

a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
    
n=len(a)
k=int(input("Enter k :"))

print(a[-k:]+a[-n:-k])

# 7) FIND SECOND LARGEST ELEMENT:

print("7) FIND SECOND LARGEST ELEMENT:")
a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

a=list(set(a))  # where we convert list to set bcze remove duplicates after that we sort & find
                 # also set not have sort() method so we convert it to list

a.sort()

print(a[len(a)-2])

# 8) MERGE TWO SORTED ARRAYS INTO ONE :

print("8) MERGE TWO SORTED ARRAYS INTO ONE :")
a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()

b=input("Enter elements: ")
b=b.split()
for i in range(len(b)):
    b[i]=int(b[i])
b.sort()

print(sorted(a+b))

# 9)Find missing number (sequence range):

print("9)Find missing number (sequence range):")
               
a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

b=max(a)
for i in range(1,b):
    if i not in a:
        print(i)

# 10)FIND TWO SUM :
               
print("# 10)FIND TWO SUM :")
               
a=input("Enter elements: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
k=int(input("Enter :"))

for i in a:
    for j in a:
        if i == j:
            continue
        if i+j==k:
            print(a.index(i),a.index(j))
    break                               
         
