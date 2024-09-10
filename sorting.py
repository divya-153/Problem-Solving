# 1) Bubble Sort:
a=[33,7,5,22,17]

for i in range(len(a)):
   for j in range(i+1, len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

# 2)Selection Sort :
a=[33,7,5,22,17]
for i in range(len(a)):
    small=a[i]
    for j in range(i+1,len(a)):

          if small > a[j]:
              small=a[j]
              s_idx=a.index(small)
          else:
              s_idx=a.index(small)
    
    temp=a[i]
    a[i]=a[s_idx]
    a[s_idx]=temp
print(a)

# 3)Insertion Sort
a = [12, 11, 13, 5, 6]
b = [a[0]]
for key in range(1, len(a)):
    if a[key] > b[-1]:
        b.append(a[key])
    else:
        
        i = len(b) - 1
        while i >= 0 and a[key] < b[i]:
            i -= 1
        b.insert(i + 1, a[key])

print(b)
        
              
          





























              
      
              
        
            
