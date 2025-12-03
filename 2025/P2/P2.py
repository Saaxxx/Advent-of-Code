# PT1
inputFile = "input.txt"

line = open(inputFile).readlines()[0]

sequences = [x.split('-') for x in line.split(",")]
print(sequences)

counter = 0

for seq in sequences:
    for i in range(int(seq[0]), int(seq[1])+1):
        stringified = str(i)
        if stringified[:(len(stringified)//2)] == stringified[(len(stringified)//2):]:
            counter += i
            
print(counter)

# PT2

line = open(inputFile).readlines()[0]

sequences = [x.split('-') for x in line.split(",")]
print(sequences)

counter = 0

print("123456789"[::2])

for seq in sequences:
    for i in range(int(seq[0]), int(seq[1])+1):
        stringified = str(i)
        # print(stringified)
            
        # patterns = set([stringified[:x] for x in range(1, (len(stringified)//2)+1)])
        
        # prim_chunks = []
        for chunk_len in range(1, (len(stringified)//2)+1):
            chunks = []
            for j in range(0, len(stringified), chunk_len):
                chunks.append(stringified[j:j+chunk_len])
                
            if (len(set(chunks)) == 1):
                # print("found", i)
                counter += i
                break
                # prim_chunks += chunks[0]
        
        # print(prim_chunks)
        # print(patterns)
            
print(counter)