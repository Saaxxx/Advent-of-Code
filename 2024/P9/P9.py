# f = open("input.txt", "r")
f = open("testinput.txt", "r")
values = list(map(int,list(f.read())))
# print(sum(values))

s = []

for i, val in enumerate(values):
    if i % 2 == 0:
      s += [str(i//2)] * val
    else:
        s +=  ["."] * val
    
# print(s)

f = open("output", "w+")
f.write("|".join(s))
# s = list(s)
# print(len(s))

f = open("output2", "w+")
start = 0
end = len(s)-1

while start < end:
    while start < end and s[start] != '.':
        start += 1
    
    while end > start and s[end] == '.':
        end -= 1
    
    if start >= end:
        break
    
    s[start] = s[end]
    s[end] = "."
    
    start += 1
    end -= 1
    
f.write("|".join(s))
# print(s)

res = 0
for i, val in enumerate(s):
    if val == ".":
        break
    res += i*int(val)
    
print(res)

s = list(values)
# s_map = []

# start = 1
# end = len(values) - (len(values) % 2)

# while start < end:
#     temp_start = start
#     while end > temp_start and int(s[temp_start]) < int(s[end]):
#         temp_start -= 2
    
#     if temp_start < end:
#         remaining = temp_start - end
        
        
    
#     start += 2
#     end -= 2

vals_dict = {}
lenghts = set()

i = 2
while i < len(s):
    val = int(s[i])
    lenghts.add(val)
    if val in vals_dict:
        vals_dict[val].append(i//2)
    else:
        vals_dict[val] = [i//2]
    
    i += 2
    
print(vals_dict)
print(lenghts)