#Exception Handling 
#Q1
a = [10,20,30]
try:
    b = int(input("enter the index"))
    print(a[b])
except:
    print("enter a valid index")
#Q2
c = {"vidit":7869593934,"cheetah":25345346}
try:
    d = input("Enter a name ")
    e = print(c.get(d))
except KeyError:
    print("name not found")
#q3
def set_age(age):
    if age < 0 or age >150:
        raise ValueError
    else:
        return age

try:
    print(set_age(-5))
except ValueError:
    print("caught error")
#q4
f = {(10,2),(5,0),(9,3)}
for i in f:
    try:
        divide = i[0]/i[1]
    except ZeroDivisionError:
        print("error caught")
    else:
        print(divide)
    finally:
        print("------")

    