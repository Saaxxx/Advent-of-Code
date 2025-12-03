import math

data = open("p6input.txt").read().strip()
lines = data.split("\n")
times = [list(map(int, x.split(":")[1].strip().split())) for x in lines]

total = 1
for i in range(len(times[0])):
    counter = 0
    for j in range(int(times[0][i])):
        if (times[0][i] - j) * j > times[1][i]:
            counter += 1
    total *= counter

print(total)

time = ""
dist = ""

for i in range(len(times[0])):
    time += str(times[0][i])
    dist += str(times[1][i])

# counter = 0
# for j in range(int(time)):
#     if (int(time) - j) * j > int(dist):
#         counter += 1
# print(counter)

# start = 0
# end = 0
# for j in range(int(time)):
#     if (int(time) - j) * j > int(dist):
#         start = j
#         break
#
# for j in range(int(time),-1,-1):
#     if (int(time) - j) * j > int(dist):
#         end = j+1
#         break
# print(end-start)
# print(start, end)

time = int(time)
dist = int(dist)
root1 = (-time+(time**2-4*dist)**0.5)/2
root2 = (-time-(time**2-4*dist)**0.5)/2

if root1 > root2:
    root1 = math.floor(root1)
    root2 = math.ceil(root2)
else:
    root1 = math.ceil(root1)
    root2 = math.floor(root2)

print(abs(root1-root2)+1)
