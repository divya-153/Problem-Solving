# 1) vowel or consonent
a=input("Enter:")
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("Vowel")
else:
    print("Consonent")

# 2) Pyramid pattern:
n=int(input("Enter rows:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end='')
    print() 

# 3) Greater 150 less than 350:
sum1=0
for i in range(150,350):
    sum1+=i
print(sum1)

# 4)concodenate string using for loop:
a=input("Enter:")
b=input("Enter:")
for i in b:
    a+=i
print(a)

# 5)reverse a string
a=input("Enter:")
print(a[::-1])
