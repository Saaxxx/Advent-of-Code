import threading
import math

def process_seed(maps, seed):
    for m in maps:
        for line in m:
            if seed in range(int(line[1]), int(line[1])+int(line[2])):
                seed += int(line[0])-int(line[1])
                break
    return seed

# def find_max_of_maps(maps, seeds):
#     max_val = max(list(map(int, seeds)))
#     for m in maps:
#         for line in m:
#             if int(line[0])+int(line[2])-1 > max_val:
#                 max_val =  int(line[0])+int(line[2])-1
#             elif int(line[0])+int(line[2])-1 > max_val:
#                 max_val = int(line[1])+int(line[2])-1
#     return max_val

f = open("p5input.txt", "r")

data = f.read().strip()

# print(data.split("\n\n")[7].split("\n"))
seeds = data.split("\n\n")[0].split(":")[1].strip().split()

maps = data.split("\n\n")[1:]
maps = [x.split('\n')[1:] for x in maps]

for m in maps:
    for x in range(len(m)):
        m[x] = m[x].split()

min_seed = math.inf

for seed in seeds:
    processed_seed = process_seed(maps, int(seed))
    if processed_seed < min_seed:
        min_seed = processed_seed

print(min_seed)

# part 2 making a single dictionary
# print("\nPart 2: THREADING")
# def thread_seeds(maps, seeds, thread_id):
#     min_seed = math.inf
#     for i in range(0, len(seeds), 2):
#         for s in range(int(seeds[i]), int(seeds[i])+int(seeds[i+1])):
#             processed_seed = process_seed(maps, s)
#             if processed_seed < min_seed:
#                 min_seed = processed_seed
#     print(min_seed, thread_id)
#
# threads = []
#
# for i in range(int(len(seeds)/2)):
#     threads.append(threading.Thread(target=thread_seeds, args=(maps,seeds[i*2:(i+1)*2],i)))
#
# for i in range(len(threads)):
#     threads[i].start()
#
# for i in range(len(threads)):
#     threads[i].join()

locations = []
for i in range(0, len(seeds), 2):
    ranges = [[int(seeds[i]), int(seeds[i])+int(seeds[i+1])]]
    results = []
    for m in maps:
        while ranges:
            start_range, end_range = ranges.pop()
            for line in m:
                dest = int(line[0])
                map_start = int(line[1])
                map_r = int(line[2])

                map_end = map_start+map_r
                offset = dest - map_start

                if map_end <= start_range or map_start >= end_range:
                    continue
                if map_start > start_range:
                    ranges.append([start_range, map_start])
                    start_range = map_start
                if map_end < end_range:
                    ranges.append([map_end,end_range])
                    end_range = map_end
                results.append([start_range+offset, end_range+offset])
                break
            else:
                results.append([start_range, end_range])
        ranges = results
        results = []
    locations += ranges
print(min(loc[0] for loc in locations))
