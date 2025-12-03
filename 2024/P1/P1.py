
f = open("input.txt", "r")
file = f.read().split("\n")

arr1 = []
arr2 = []

# pt1
# for line in file:
#     ints = line.split("   ")
#     arr1.append(int(ints[0]))
#     arr2.append(int(ints[1]))
    
    
# arr1.sort()
# arr2.sort()

# diff = [abs(arr1[i]-arr2[i]) for i in range(len(arr1))]
# print(sum(diff))



# pt2
dict2 = {}
for line in file:
    ints = line.split("   ")
    arr1.append(int(ints[0]))
    
    if int(ints[1]) in dict2:
        dict2[int(ints[1])] += 1
    else:
        dict2[int(ints[1])] = 1
        
res = 0
for num in arr1:
    if num in dict2:
        res += num * dict2[num]
    # print(res)
        
print(res)