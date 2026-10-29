#Exception Handling
#q1
with open("quote.txt","w") as file:
    file.write("i know i will do it man maybe i cooked rn but i will do it surely")

with open("quote.txt","r") as file:
    file.read()

#q2
file = open("quote.txt","a")
for i in range(0,3):
    file.write("hello\n")
file.close()
#q3
a = open("quote.txt","r")
b =a.readlines()
print(len(b))
a.close()