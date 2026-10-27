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