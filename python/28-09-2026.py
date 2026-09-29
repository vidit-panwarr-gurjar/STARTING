#1
a = "pymaster india"
print(a.upper())
print(a.title())
#2
b = " clean this "
print(len(b))
b = b.strip()
print(b)
print(len(b))
#3
c = "12345"
print(c.isdigit())
d = "hello123"
print(c.isalpha())
#4
e = "this is bad code with bad habits"
print(e.replace("bad","good"))
#5
f = "one:two:three"
print(f.split(":"))
#6
g = ["Python","is","fun"]
print(" ".join(g))
#7
h = "Python"
print(h.startswith("Py"))
print(h.endswith("on"))
#8
i = "                     vidit             "
print(i.rjust(30))
#9
j = '7'
print(j.zfill(4))
#10
k= "vidit"
l = 8.5
print(f"my name is {k} and my score is {l}")
#11
m = "PyMaster India"
print(m.find('India'))
print(m.index('India'))
#12
n = "banana"
print(n.count('an'),n.count('a'))
#13
o = 'Rajeev,25,Varanasi,Python'
print(o.split(','))
#14
print("{:<15}{:<10}{:<10}".format('Item','Quantity','Price'))
print("{:<15}{:<10}{:<10}".format('1','25','500'))
print("{:<15}{:<10}{:<10}".format('2','30','1000'))
#15
p = '***hello world***'
print(p.strip('*'))
#new shit 
print(1+2 == 3)
print(2%3)
#more new shit 
a = 'abc'
print(bool())   
