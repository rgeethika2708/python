r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

a = []

print("Enter matrix elements:")
for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

print("Transpose of matrix:")

for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()
