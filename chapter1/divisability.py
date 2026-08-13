n=int(input("enter number"))
if n%3==0 and n%5==0:
    print("n is divisible by 3 and 5")
elif n%5==0:
    print("n is divisible by 5")
elif n%3==0:
    print("n is divisible by 3")
else:
    print(n)            
