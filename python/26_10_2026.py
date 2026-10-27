#1
def multiply(*args):
    ans = 1
    for i in args:
        ans = ans*i
    return ans

print(multiply(2,3,4,5))
#2
def how_many(*args):
    count = 0
    for i in args:
        count = count + 1
    return count
print(how_many(5,4,33))
#3
def describe(**kwargs):
    print("name is ",kwargs["name"])
    print("age is ",kwargs["age"])

print(describe(name = "vidit", age = 19))
#4
def max(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    return max
print(max(5,6,3,2,4))
#5
def add3(a,b,c):
    return a+b+c

nums = [4,5,6]
print(add3(*nums))
#6

    


