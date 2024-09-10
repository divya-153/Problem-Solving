# 1)Factorial :
a=int(input("Enter:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

# 2)prime number :

a=int(input("Enter :"))
flag=0
for i in range(2,a):
    if (a%i)==0:
        flag=flag+1
if flag==0:
    print("Prime")
else:
    print("Non-Prime")

# 3)Fibonacci series :
n=int(input("Enter :"))
n1,n2=0,1

for i in range (n):
   
  print(n1,end=",")

  temp=n1+n2
  n1 = n2
  n2 = temp

# 4)REVERSE AN INTEGER:
a=int(input("Enter:"))
b=str(a)
print(int(b[::-1]))

# 5)Palidnrome :

a=int(input("Enter :"))
b=str(a)
b=int(b[::-1])
if a==b:
    print("Palindrome ")
else:
    print("Not ")

# 6)GCD :

a=int(input("Enter :"))
b=int(input("Enter :"))

cf=[]

for i in range(2,min(a,b)):
    if a%i==0 and b%i==0:
        cf.append(i)
print(max(cf))

# 7) LCM :

a=int(input("Enter :"))
b=int(input("Enter :"))

cf=[]

for i in range(2,min(a,b)):
    if a%i==0 and b%i==0:
        cf.append(i)
gcd=max(cf)
print("LCM: ",(a*b)//gcd) 

# 8)COUNT DIGITS IN A NUMBER:

a=int(input("enter :"))
print(len(str(a)))

# 9) SUM OF DIGITS:
a=int(input("Enter :"))
a=str(a)
add=0

for i in a:
    add=add+int(i)
print(add)

# 10)DECIMAL TO BINARY :

a=int(input("Enter :"))
print(bin(a)[2:])













































