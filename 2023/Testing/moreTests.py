import math

x = 108738449*131
m = 1000000007
xm = x%m

print(x)
print(xm)

def hash(password):
    res = 0
    for i,x in enumerate(password):
        res = (res + ord(x)*math.pow(131, len(password)-1-i))%m
        
    return int(res)

# print(hash("00000")*131%m)
print(hash("cAr1"))
print(hash("cAr1g"))

print()
print(hash("00000000A"))