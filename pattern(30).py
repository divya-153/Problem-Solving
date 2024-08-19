# 1) Square pattern:

n=int(input("Enter rows:"))
print()

print("Square pattern:")
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()

# 2) hollow square pattern:

print("hollow square pattern:")
for i in range(1,n+1):
       
        if i==1 or i==n:
            for j in range(n+1):
              print("*",end="")

        else:
            print("*",end="")
            for k in range(n-1):
                print(" ",end="")
            print("*",end="")

        print()

# 3)left triangle pattern:

print("left triangle pattern:")

for i in range(1,n+1):

    for j in range(1,2*i):
        print("*",end="")
    print()

# 4)right triangle:

print("right triangle:")

for i in range(1,n+1):

    for j in range(2*(n-i)):
        print(" ",end="")

    for k in range(1,2*i):
        print("*",end="")
    print()

# 5)left down triangle:

print("left down triangle pattern:")

for i in reversed(range(1,n+1)):

    for j in range(1,2*i):
        print("*",end="")
    print()
# 6)right down triangle:

print("right down triangle:")

for i in reversed(range(1,n+1)):

    for j in range(2*(n-i)):
        print(" ",end="")

    for k in range(1,2*i):
        print("*",end="")
    print()

# 7)Hollow left triangle star pattern 

print("Hollow left triangle star pattern ")

for i in range(1,n+1):

    if i==1 or i==n:
      for j in range((i*2)-1):
            print("*",end="")

    else:
        print("*",end="")
        for k in range ((2*i)-3):
            print(" ",end="")
        print("*",end="")
    print()

#  ii) Hollow right triangle star pattern
print("Hollow right triangle star pattern ")

for i in range(1,n+1):
    for y in range(2*(n-i)):
        print(" ",end="")

    if i==1 or i==n:
      for j in range((i*2)-1):
            print("*",end="")

    else:
        print("*",end="")
        for k in range ((2*i)-3):
            print(" ",end="")
        print("*",end="")
    print()

# 8)pyramid star pattern:

print("Pyramid star patter:")

for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()

# 9)Reversed pyramid

print()
print("9)Reversed pyramid")

for i in reversed( range(1,n+1)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()
    
# 10)Hollow pyramid pattern

print()
print("10) Hollow pyramid pattern")

for i in range(1,n+1):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1 or i==n:
        for j in range((2*i)-1):
            print("*",end="")
    else:
        print("*",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("*",end="")
    print()

# 11)Diamond star pattern

print()
print("Diamond star pattern")

for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()
for i in reversed( range(1,n)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()

#12) Hollow diamond star pattern 

print()
print("10)Hollow diamond star pattern")
# 1st
for i in range(1,n+1):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
        for j in range((2*i)-1):
            print("*",end="")
    else:
        print("*",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("*",end="")
    print()
#2nd
for i in reversed(range(1,n+1)):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
        for j in range((2*i)-1):
            print("*",end="")
    else:
        print("*",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("*",end="")
    print()

#13)Hourglass star pattern

print()
print("13)Hourglass star pattern:")

#1st
for i in reversed( range(1,n+1)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()
#2nd
for i in range(2,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()

#14) Right pascal star pattern
print()
print("14) Right pascal star pattern")

for i in range(1,n+1):

  for j in range(i):
      print("*",end="")
      
  print()
for i in reversed(range(1,n)):

  for j in range(i):
      print("*",end="")
      
  print()

#15)left pascal star pattern
print()
print("15) left pascal star pattern")

for i in range(1,n+1):

  for k in range(n-i):
    print(" ",end="")

  for j in range(i):
      print("*",end="")
      
  print()
for i in reversed(range(1,n)):

  for k in range((n-i)):
    print(" ",end="")
  for j in range(i):
      print("*",end="")

  print()

# 16)Heart Pattern :
print()
print("16) Heart pattern")
a=int(n/2)
print(" ",end="")
for i in range(a):
    print("*",end="")
for i in range(3):
    print(" ",end="")
for i in range(a):
    print("*",end="")
print()
for i in range(a+2):
    print("*",end="")
for i in range(1):
    print(" ",end="")
for i in range(a+2):
    print("*",end="")
print()


for i in reversed( range(1,n+1)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print("*",end="")
    print()
    

# 17)plus pattern :
print()
print("17)plus pattern ")
import math
a=n/2
a=math.ceil(a)

for i in range(1,n+1):
    if i!=a:
        for j in range(a-1):
            print(" ",end="")
        print("*")
        
    else:
        for j in range(n):
            print("*",end="")
        print()

# 18)Cross pattern program :

print()
print("18) Cross pattern program ")
for i in reversed(range(1,n+1)):
       for j in range(n-i):
              print(" ",end="")

       print("X",end="")
       for k in range((2*i)-3):
           print(" ",end="")
       if i!=1:
        print("X",end="")

       print()    
for i in (range(1,n+1)):
       for j in range(n-i):
              print(" ",end="")

       print("X",end="")
       for k in range((2*i)-3):
           print(" ",end="")
       if i!=1:
        print("X",end="")

       print() 

# 19)left triangle number pattern:

print()
print()
print("19)left triangle number pattern:")

for i in range(1,n+1):

    for k in range(1,2*i):
        print(k,end="")
    print()

# 20)Right triangle:

print()
print("19)right triangle number pattern:")

for i in range(1,n+1):

    for j in range(2*(n-i)):
        print(" ",end="")

    for k in range(1,2*i):
        print(k,end="")
    print()

# 21) Number pyramid pattern :
print()
print()
print(" 21) Number pyramid pattern")

for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(k,end="")
    print()
# 22) Number pyramid reverse pattern:

print(" 22) Reversed Number pyramid pattern")
print()
for i in reversed(range(1,n+1)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(k,end="")
    print()

# 23) Number hollow pyramid pattern

print()
print("23) Number hollow pyramid pattern")
print()

for i in range(1,n+1):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1 or i==n:
        for j in range(1,2*i):
            print(j,end="")
    else:
        print("1",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("2",end="")
    print()

# 24) Number diamond pattern

print()
print("24. Number diamond pattern")
print()

for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(k,end="")
    print()
for i in reversed( range(1,n)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(k,end="")
    print()

#25. Hollow number diamond pattern:
print()
print("25. Hollow number diamond pattern")
print()

# 1st
for i in range(1,n+1):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
         print("1",end="")
    else:
        print("1",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("2",end="")
    print()
#2nd
for i in reversed(range(1,n+1)):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
            print("1",end="")
    else:
        print("1",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("2",end="")
    print()

# 26) Alphabet pyramid pattern
print()
print("26) Alphabet pyramid pattern")
print()

for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(chr(k+64),end="")   # chr() used for convert ASCII code into alphabets 
    print()

# 27) Alphabet reversed pyramid pattern
print()
print("27) Alphabet reversed pyramid pattern")
print()

for i in reversed(range(1,n+1)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(chr(k+64),end="")   # chr() used for convert ASCII code into alphabets 
    print()
      

    
# 29)Alphabet diamond pattern
print()
print("29) Alphabet diamond pattern")
print()


for i in range(1,n+1):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(chr(k+64),end="")   # chr() used for convert ASCII code into alphabets 
    print()

for i in reversed(range(1,n)):

    for j in range(n-i):
       print(" ",end="")
       
    for k in range(1,2*i):
        print(chr(k+64),end="")   
    print()
      
# 30)Hollow alphabet diamond pattern:
print()
print("30) Hollow alphabet diamond pattern")
print()

# 1st
for i in range(1,n+1):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
         print("A",end="")
    else:
        print("A",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("B",end="")
    print()
#2nd
for i in reversed(range(1,n+1)):
    
    for j in range(n-i):
              print(" ",end="")

    if i==1:
            print("A",end="")
    else:
        print("A",end="")
        for k in range((2*i)-3):
            print(" ",end="")
        print("B",end="")
    print()

# 31) continuous number printing: 5=>25,
print()
print("31) continuous number printing")
print()
a=1
for i in range(1,n+1):
    for j in range(1,2*i):
        print((a),end="")
        a=a+1
        
    print()

# 32) 1 222 33333 kind pattern :
print()
print("32) 1 222 33333 kind pattern :")
print()

for i in range(1,n+1):
    for j in range(1,2*i):
        print(i,end="")
    print()


# if we need

"""
1
123
12345
1234567    => give print(j)     
123456789

1
234
56789
10111213141516           a=1
171819202122232425  => give print(a)
                         a=a+1

1
222
33333             => print(i)
4444444
555555555"""
    
# 33) continuous alphabet left triangle pattern:
print()
print("33)  continuous alphabet left triangle pattern")
print() 

a=65
for i in range(1,n+1):
    for j in range(1,2*i):
        print(chr(a),end="")
        a=a+1
    print()

# 34)Pyramid continuous albhapet:
print()
print(" 34) Pyramid continuous albhapet")
print()

a=65
for i in range(1,n+1):
    for b in range(n-i):
       print(" ",end="")
    for j in range(1,2*i):
        print(chr(a),end="")
        a=a+1
    print()

# 28)Hollow pyramid continuous alphabet:
print()
print("28) hollow pyramid continuous alphabet")
print()

a=65
for i in range(1,n+1):
    for b in range(n-i):
       print(" ",end="")
    for j in range(1,2*i):
     if i!=(n):
        if j==1 or j==((2*i)-1):
          print(chr(a),end="")
          a=a+1
        else:
            for k in range((2*i)-3):
              print(" ",end="")
              break    #for break multiple executions cause of nested for loop
     else:
        print(chr(a),end="")
        a=a+1
    print()
























    
    












