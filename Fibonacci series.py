#FIBONACCI SERIES
num = int(input("Enter amount of number : "))

a=0
b=1
c=0
print("Fibonacci series = ")
while c<num+1:
    a=b
    b=c
    c=a+b
    print(f"{c} , ",end="")