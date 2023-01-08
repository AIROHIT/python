mylist = ['apple', 'banana', 'cherry']
mylist.append('orange')
print(mylist)

mylist = ['apple', 'banana', 'cherry']
mylist.insert(1, 'orange')
print(mylist)

mylist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
mylist.extend(tropical)
print(mylist)

mylist = ['apple', 'banana', 'cherry']
thistuple = ('kiwi', 'orange')
mylist.extend(thistuple)
print(mylist)

mylist = ['apple', 'banana', 'cherry']
for x in mylist:
    print(x+' ',end="")
print('')

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i]+' ',end="")
    i = i+1
print('')

a = 200
b= 33
if b > a:
    print('b is greater than a')
elif a ==b :
    print('a and b are equal')
else:
    print('a greater then b')

a = 2
b= 3
print("a") if a>b else print("b") 

a = 33
b = 33
print('a') if a>b else print('both') if a==b else print('b') 

a=200
b=33
c=500
if a>b and c>a:
    print('Both condition are true')



    i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

    mylist = ['apple', 'banana', 'cherry']
mylist.append('orange')
print(mylist)

mylist = ['apple', 'banana', 'cherry']
mylist.insert(1, 'orange')
print(mylist)

mylist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
mylist.extend(tropical)
print(mylist)

mylist = ['apple', 'banana', 'cherry']
thistuple = ('kiwi', 'orange')
mylist.extend(thistuple)
print(mylist)

mylist = ['apple', 'banana', 'cherry']
for x in mylist:
    print(x+' ', end="")
print('')

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i]+' ', end="")
    i = i+1
print('')

a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a greater then b')

a = 2
b = 3
print("a") if a > b else print("b")

a = 33
b = 33
print('a') if a > b else print('both') if a == b else print('b')

a = 200
b = 33
c = 500
if a > b and c > a:
    print('Both condition are true')

a = 200
b = 100
if a > b:
    if a % b == 0:
        print('Satisfied')
    else:
        print('Not satisfied')

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

for x in 'banana':
    print(x)

for x in range(6):
    print(x)

obj = ['red','big','tasty']
fruits = ['apple','banana','charry']
for x in obj:
    for y in fruits:
        print(x, y)

def my_fun(fname):
    print(fname+' is tasty')


    def my_function(fname):
    print(fname + "Refsname")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil","Refsnes")

def my_function(*kids):
    print("The youngest child is "+kids[2])
my_function("Emil","Tobias","Linus")

def my_function(child3,child2,child1):
    print("The youngest child is "+child3)
my_function(child1 = "Emil", child2="Tobias", child3="Linus")

def my_function(**kid):
    print("His last name is "+kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
    print("I am from "+country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Bazil")

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","bannana","cherry"]
my_function(fruits)

def my_function(x):
    return 3*x
    print(my_function(3))
    print(my_function(5))
    print(my_function(9))