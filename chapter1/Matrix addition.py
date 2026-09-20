r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
B = []

print("Enter first matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter second matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result:")
for row in C:
    print(*row)
