num = int(input("Enter number :"))

print(f"{num} divisible by ")
for i in range(1,num+1):
    if num%i==0:
        print(f"{i} , " , end="")
