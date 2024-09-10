# 1)Linear Search:
a=[2,3,4,10,40]
key=int(input("Enter :"))
flag=0
for i in a:
 if key==i:
        print("Yes : The Position:",a.index(key))
        flag=1

if flag==0:
    print("Element not present in array")

# 2)Binary search:
a=[2,3,4,10,40]
key=int(input("Enter :"))
left=0
right=len(a)-1
flag=0
while(left<=right):
    mid=int(left+(right-left)/2)
    if a[mid]==key:
        print("Yes : The Position:",a.index(key))
        flag=1
    if a[mid]<key:
              left=mid+1
    else:
        right=mid-1
if flag==0:
    print("Element not present in array")
