chice = int(input("Enter 1 for c to f \t enter 2 for f to c\v"))

if chice == 1:
    c=int(input("Enter temparature in calcius : "))
    f=((c/5)*9)+32
    print(f"Tempareture in farenhit = {f} f")
elif chice == 2:
    f=int(input("Enter temparature in farenhit : "))
    c=((f-32)*5)/9
    print(f"Temparature in calcius = {c} c")
else:
    print("You didn't change any option")

