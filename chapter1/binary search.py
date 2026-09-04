def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
          return mid
        elif arr[mid]<key:
           low=mid+1
        else:
            high=mid-1
    return -1
arr=[10,23,24,56]
key=90
result=binarysearch(arr,key)
if result!=-1:
  print("enter element found at index",result)
else:
  print("element not found")
