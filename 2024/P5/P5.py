# f = open("testinput.txt", "r")
f = open("input.txt", "r") 
[keys, records] = f.read().split("\n\n")


mustBeBefore = {}
mustBeAfter = {}

for key in keys.split("\n"):
    # print(key.split("|"))
    [k, v] = key.split("|")
    if (k in mustBeAfter):
        mustBeAfter[k].add(v)
    else:
        mustBeAfter[k] = set()
        mustBeAfter[k].add(v)
        
    if (v in mustBeBefore):
        mustBeBefore[v].add(k)
    else:
        mustBeBefore[v] = set()
        mustBeBefore[v].add(k)
    
res = 0

invalidRecords = [] 

# print(mustBeAfter)
# print(mustBeBefore)

for record in records.split("\n"):
    record = record.split(",")
    beforeCurrentIndex = set()
    afterCurrentIndex = set(record)
    
    valid = True
    for val in record:
        afterCurrentIndex.remove(val)
        for aft in afterCurrentIndex:
            if (val in mustBeBefore and aft in mustBeBefore[val]):
                valid = False
                # print("invalid aft", aft, mustBeBefore[val], val)
                invalidRecords.append(record)
                break
            
        if not valid:
            break
        
        for bef in beforeCurrentIndex:
            if (val in mustBeAfter and bef in mustBeAfter[val]):
                valid = False
                # print("invalid bef")65
                invalidRecords.append(record)
                break
       
        beforeCurrentIndex.add(val)
        
    else:
        res += int(record[len(record)//2])
        
print(res)
    
res = 0
for record in invalidRecords:
    # print("rec",  record)
    counts = {}
    s = set(record)
    for val in record:
        s.remove(val)
        
        counts[val] = 0
        
        if (val in mustBeAfter):
            # print("mba", val, mustBeAfter[val])
            # print("mbb", 53, mustBeBefore["53"])
            for v in s:
                if v in mustBeAfter[val]:
                    counts[val] += 1
            # print(counts)
            if counts[val] == len(record)//2:
                # print(record, counts, "   ", val)
                res += int(val)
                break
        
        
        s.add(val)

# print(counts)
print(res)