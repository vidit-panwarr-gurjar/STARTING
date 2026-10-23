#q1
a = [i*i for i in range(1,11)]
b = [j*j for j in range(1,11) if j%2==0]
print(a,b)
#q2
c={i:i*i*i for i in range(1,7)}
print(c[4])
#q3
d = input('enter your name')
e = {i for i in d if d in 'aeiou'}
#q4
