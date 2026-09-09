list=[1,3,2,4,2,3]
newlist=[]
for i in list:
  if i not in newlist:
    newlist.append(i)
print(newlist)    
