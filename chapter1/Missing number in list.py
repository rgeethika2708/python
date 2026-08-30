n = int(input("Enter N: "))
a = list(map(int, input("Enter the numbers: ").split()))

total = n * (n + 1) // 2
sum_list = sum(a)

missing = total - sum_list

print("Missing number:", missing)
