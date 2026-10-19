#q1
a  = [4,1,2,2,3,4,5,1]
b =  list(set(a))
print(b)
#q2
c = ("Amit",21,"BCA",8.5)
name,age,course,gpa = c
print(f"{name} {age} studies {course} with gpa {gpa}")
#q3
d ={'Ravi','sara','Deep','Amit'}
e ={'Sara','Amit','neha'}
print(d & e)
print(d | e)
#q4
a,b = 1,2
a,b = b,a
