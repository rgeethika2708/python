a = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target sum: "))

print("Pairs are:")

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])
