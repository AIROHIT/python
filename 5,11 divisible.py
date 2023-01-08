a=int(input("Enter number : "))

if((a%5==0)and(a%11!=0)):
    print(f"Your enter number {a} divisible by 5")
elif((a%5!=0)and(a%11==0)):
     print(f"Your enter number {a} divisible by 11")
elif((a%5==0)and(a%11==0)):
     print(f"Your enter number {a} divisible by 5 and 11 both")
else:
     print(f"Your enter number {a} not divisible by 5 and 11")
     