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
