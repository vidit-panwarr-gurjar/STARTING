#list 
#q1
a =[10,20,30,40,50]
print(a[0],a[-5],a[4],a[-1])
#q2
b = [45,67,89,23,90,56,87]
print(b[0:3])
print(b[-1:-3])
print(b[::2])
print(b[::-1])
#q3
c = ["wake up","Study"]
c.append("exercise")
print(c)
c.insert(0,"medidate")
print(c)
c.insert(-1,'sleep')
print(c)
#q4
d=[["vidit",100],["DC",100],["VIKI",100]]
print(d[1][0],d[2][1])
#q5
e = [101,'Vranasi',25.3,82.9]
id,city,lat,lon = e 
print(f"my id is {id} and i live in {city} whereas my lat and lon are {lat} {lon}")




