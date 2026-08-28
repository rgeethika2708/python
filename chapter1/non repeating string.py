s=input("enter string:")
for ch in s:
    if s.count(ch)==1:
       print("first non repeating character:",ch)
else:
     print("not found")
