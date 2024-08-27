""" s={1,2,3,4,5,6,7,8,9}
s=list(s)
l=len(s)
mid=l//2
start=0
end=l
lis=[]

def binary(arr,target,start,end):
    mid=len(arr)//2
    print(mid,"mid",start,end)
    if arr[mid]==target:
        print(arr[mid],mid)
    else:
        if arr[mid]>target:
            end=mid
        elif arr[mid]<target:
            start=mid
        for x in range(start,end+1):
            lis.append(x)
        binary(lis,target,start,end)

binary(s,2,start,end) """
""" 
def binary_search(arr, target, start, end):
    if start >= end:
        return -1  # Target not found

    mid = (start + end) // 2
    print(mid, "mid", start, end)

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid)
    else:
        return binary_search(arr, target, mid + 1, end)

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = binary_search(s, target, 0, len(s))

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found") """


""" lis=[1,2,3,4,5,6,7,8,9]
target=5
for x in range(len(lis)):
    if lis[x]==target:
        print(target,"got found in the place of index",x) """

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

a=[]
b=[]

for x in range(7):
    if x%2==0:
        b.append(l2[x])
    else:
        a.append(l1[x])
print(a,b)
a.extend(b)
print(a)