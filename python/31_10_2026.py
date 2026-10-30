#python modules and packages
#Q1
import random as rm
for i in range(1,7):
    print(rm.randint(1,7))
#Q2
import datetime as dt

print(dt.date.today())
print(dt.datetime.now().year)
#Q3
import greetings as gt
print(gt.hello("yes"))

#Q4
from utils.numbers import is_even
print(is_even(34))
from utils.strings import shout
print(shout("abc"))

#Q5
a = int(input("enter the length of the passowrd you need"))
print(rm.randint(0,a))

