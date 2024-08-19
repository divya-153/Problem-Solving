"""# 1) Reverse a String:

a=input("Enter :")
print(a[::-1])

# 2)Palindrome:
palindrome:
a=input("Enter string:")
b=''.join(reversed(a))
if a==(a[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")

# 3)FIRST NON-REPEATED CHARACTER :
from collections import Counter
a=input("Enter :")
c=Counter(list(a))

for key in c:
    if c[key]==1:     # for access value => c[key] represent value in c:
       print(key)
       break

# 4)REMOVE DUPLICATE CHARACTERS :
a=input("Enter :")
a=list(a)
a1,a2="",""
for i in a:
    if i not in a1:
        a1+=i
    elif i not in a2:
        a2+=i
print(a1)

# 5)COUNT VOWELS AND CONSONENTS :
a=input("Enter :")
vowel,cons=0,0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel=vowel+1
    else:
        cons=cons+1
print("vowel :",vowel)
print("Consonent :",cons)

# 6)FIND LONGEST WORD
from collections import Counter
a=input("Enter :")
a=a.split()
long=0

for i in a:
    if len(i)>long:
        long=len(i)
        word=i
print(word)

# 7)FIND ALL SUBSTRINGS:

a=input("Enter :")

# 8)COUNT OCCURENCES of  a given character in string:

from collections import Counter
a=input("Enter :")
n=input("Enter char :")
c=Counter(a)

for key in c:
    if key==n:
        print(key, ":" , c[key])

# 9)CONVERT TO UPPERCASE:
a=input("Enter :")
print(a.upper())

# 10)ANAGRAMS
a=input("Enter :")
a=''.join(sorted(a))

b=input("Enter :")
b=''.join(sorted(b))

if a==b:
    print("Anagram")
else:
    print("not")"""



   
