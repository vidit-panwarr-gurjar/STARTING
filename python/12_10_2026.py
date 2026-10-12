#Wap a program to display all natural numbers

for i in range(1,10):
    print(i)

#Wap a program to print table of n upto 10

n = int(input("enter your number"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

i = 1


while i<=10:
    print(f"{n} * {i} = {n*i}")
    i = i + 1

#WAP a program to print sum of numbers for 1 to 100 

sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

#Wap a program to print even numbers from 1 to 20 using continue

for i in range (1,21):
    if i%2 != 0:
        continue
    print(i) 