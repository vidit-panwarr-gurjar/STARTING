#defining sum and avg of a list

def sum_n_avg(num,avg,sum):
    for i in num:
        sum = sum + i

    avg = sum/len(num)
    return sum,avg

print(sum_n_avg([2,3,4,5],0,0))

#finding simple interest

def simple_interest(p,t,r =5):
    return (p*r*t)/100

print(simple_interest(5,5))

#finding grades

def finding_grades(grade):
    if grade > 80:
        return "A"
    elif grade > 60:
        return "B"
    elif grade > 40:
        return "C"
    else:
        return "D"

print(finding_grades(97))

#temperature converter

def convert(temp,to="F"):
    if to == "F":
        return temp*9/5 + 32
    else:
        return(temp-32)*5/9

print(convert(64,"F"))
print(convert(147.2))
