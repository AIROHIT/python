A=int(input("Enter a number :"))

sum=0
temp = A
while A>0 :
    b=A%10
    sum = sum + (b**3)
    A = A//10

if(temp==sum):
    print(f"Enter number {temp} is a armstrong number ")
else:
    print(f"Enter number {temp} is not a armstrong number ")