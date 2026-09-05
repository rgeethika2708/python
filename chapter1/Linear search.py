def linearsearch(arr,target):
    for i in range(len(arr)):
       if arr[i]==target:
          return i
    return -1
numbers=[12,13,16,20,78]
result=linearsearch(numbers,16)
if result!=-1:
        print("element found at index:",result)
else:
    print("element not found")
  
