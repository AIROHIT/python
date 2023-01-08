a=int(input("Enter your number : "))
b=1

if(a==0):
    print("factorial of this number : 1 ")
else:
    for i in range(1,a+1):
         b=b*i
    print("factorial of this number",b)

