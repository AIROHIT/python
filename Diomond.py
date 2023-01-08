row = int(input("Enter row number : "))

for i in range(1,row+1):
    for j in range(1,(row-i)+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print("\r")
for i in range(0,row+1):
    for space in range(0,i+1):
        print(" ",end="")
    for j in range(1,row-i):
        print("* ",end="")
    print("\r")