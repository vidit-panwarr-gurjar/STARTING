def add(a,b):
    print("sum is", a+b)

print(add(5,10))
#q1
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
a = int(input("enter a number to check"))
print(is_even(a))
print(is_even(10))
def find_area(b,c):
    print("area of the recatangle is",b*c)
print(find_area(10,13))

def find_max(d,e,f):
    if d>e and d>f:
        return d
    elif e>d and e>f:
        return e
    else:
        return f

print(find_max(2,3,4))


    