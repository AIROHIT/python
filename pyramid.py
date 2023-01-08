a=int(input("Enter pyramid row : "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("* ",end="")
    print("\r")
