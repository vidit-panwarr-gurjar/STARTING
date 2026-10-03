#Wap to check wheater number is positive negative or zero
num = int(input("enter the number"))
if num == 0:
    print("it isnt positve nor negative")
elif num > 0:
    print("number is positive")
else:
    print("number is negative")
#WAP to check whether it is even or odd
num2 = int(input("enter the second number"))
if num2 % 2 == 0:
    print("number is even")
else:
    print("number is odd")
#WAP to give grade to a student 
marks = int(input("enter your marks"))
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 60:
    print("C grade")
else:
    print("failed")
#wap to print greatest number out of 3
num3 = int(input("enter the num1"))
num4 = int(input("Enter the num2"))
num5 = int(input("enter the num3"))
if num3 > num4:
    if num3 > num5:
        print(f"{num3} is the greatest")
elif num4 > num5:
    if num4 > num3:
        print(f"{num4} is the greatest")
else:
    print(f"{num5} is the greatest")


