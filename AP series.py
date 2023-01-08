num=int(input("Enter amount of number "))

sum=0
print(f"Numbers are = ")
for i in range(0,num+1):
    print(f"{i},",end="")
    sum = sum + i
print(sum)
