def pat( row):
    if(row == 0):
        return
    print("*",end="")
    pat(row - 1)


row = int(input("Enter row number >> "))

for i in range (0,row+1):
    pat(i)
    print("\r")

