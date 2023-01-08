row = int(input("Enter row number : "))

for i in range(0,row+1):
    for space in range(1,i+1):
        print(" ",end="")
    for j in range(0,row-i):
        print("* ",end="")
    print("\r")