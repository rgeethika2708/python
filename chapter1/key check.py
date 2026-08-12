d={}
n=int(input("enter no.of items"))
for i in range(n):

    key=input("enter key")
    value=input("enter value")
    d[key]=value
searchkey=input("enter key to check")


if searchkey in d:
    print("key exists in the dictionary")
else:
    print("key does not exist in the dictionary")    
