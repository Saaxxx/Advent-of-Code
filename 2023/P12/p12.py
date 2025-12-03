def find_arrangements(line, seg):
    
    seg = list(map(int, seg.split(",")))
    line = [x for x in line]
    
    # for i,l in enumerate(line):
        
    #     counter = 0
    #     if l == "?":
    #         for j in range(seg[counter]):
    #             # try insert the ?
    #             line[i:]
    
    # prev = ""
    # counter = 0
    # q_segs = []
    # hash_segs = []
    # for i,l in enumerate(line):
    #     if l == "?" or l == "#":
    #         counter += 1
            
    #     elif prev == "?" and l != "?":
    #         q_segs.append([i-counter, i-1])
    #         counter = 0
            
    #     elif prev == "#" and l != "#":
    #         hash_segs.append([i-counter,i-1])
    #         counter = 0
        
    #     prev = l
    
    # if prev == "#":
    #     hash_segs.append([len(line)-counter,len(line)-1])
    # elif prev == "#":
    #     q_segs.append([len(line)-counter,len(line)-1])
        
    prev = ""
    counter = 0
    segs = []
    for i,l in enumerate(line):
        if l == "?" or l == "#":
            counter += 1
            
        elif prev == "?" and l != "?":
            segs.append([prev, i-counter, i-1])
            counter = 0
            
        elif prev == "#" and l != "#":
            segs.append([prev, i-counter,i-1])
            counter = 0
        
        prev = l
    
    if prev == "#" or prev == "#":
        segs.append([prev, len(line)-counter,len(line)-1])
        
    print(segs)
    
    return 0





f = open("test.txt", "r").read().strip()

lines = [x.split(" ")[0] for x in f.split("\n")]
segs = [x.split(" ")[1] for x in f.split("\n")]

# for i,x in enumerate(lines):
#     find_arrangements(x, segs[i])
    
find_arrangements(lines[0], segs[0])