from random import shuffle

x = 0
y = 0
z = 0

print(x == 0 and y == 1 and z == 0)


l = [1,1,2,3,4]

print(l[:-1])

d = {x:l.count(x) for x in l}
print(d[1])
if 3 in d:
    print(d)
    
a = "nat"
b = "tan"

d = {x:a.count(x) for x in a}
e = {x:b.count(x) for x in b}
print(d)
print(e)
print(d==e)

d['e'] = 0
print(d)


d = []
if ' ' in d:
    print("no")

print([0]*256)
print(ord('x'))

l = [1,2,3,4,5]
print(l[0:])

shuffle(l)

print(l)

def bubblesort(l):
    
    if l == None:
        return l
    
    for i in range(len(l)-1,0,-1):
        for j in range(0,i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    
    return l

l = bubblesort(l)

print(l)

p = {1:2}

print(int(not 0))