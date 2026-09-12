lst = [10, 25, 5, 40, 30]

largest = lst[0]
second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest element:", second)
