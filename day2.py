#1) Count vowels in a string:
st=input("Enter:")
count=0
for a in st:
  if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    count+=1
print(count)
# 2) Check 2 strings are anagram or not

a=list(input("Enter:"))
b=list(input("Enter:"))
if a.sort()==b.sort():
    print("Anagram")
else:
    print("not")

# 3) Automorphic :
a=int(input("Enter:"))
b=a*a
c=str(b)
n=len(str(a))
if a==int(c[-n:]):
    print("yes")
else:
    print("No")

# 4)Isomorphic:

# Method 1:
from collections import Counter
a=input("Enter :")
c=Counter(a)
flag=0
for key in c:
    if c[key]!=1:
        flag+=1
if flag==0:
    print("Isomorphic")
else:
    print("Not")

# Method 2:
a=input("Enter :")
a1,a2=[],[]
for i in a:
    if i not in a1:
        a1.append(i)
    else:
        a2.append(i)
if a2==[]:
    print("Isomorphic")
else:
    print("No")
























