#q1
a = {"vidit":1449034890348,"cheetah":43832908290,"sher":298573247}
b = input("enter a name")
print(a.get(b,"not found"))
#q2
c = {"math":90,"sci":85,"eng":78}
max = 0
sum = 0
for d in c:
    if max < c[d]:
        max = c[d]
    sum = sum + c[d]
print(sum,max)
#q3
e = {"name":{"vidit":10,"cheetah":11,"mere":12}}
max = 0
for i in e["name"]:
    if e["name"][i] > max:
        max = i
print(max)