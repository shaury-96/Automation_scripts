import random
l="abcdefghijklmnopqrstuvwxyz"
u=l.upper()
n="0123456789"
s="[]{}()*;/,_-@"
a=l+n+s
len=8

for i in range(100000):
    pas="".join(random.sample(a,len))
    if(pas=="shaury@123"):
        print(pas)
        break


print("not found",pas)