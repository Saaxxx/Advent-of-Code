import re

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_first_number(line):

    val = 0
    first_index = len(line)
    for num in nums:
        if line.find(num) < first_index and line.find(num) != -1:
            val = nums.index(num)+1
            first_index = line.find(num)

    for i in range(first_index):
        if line[i] > '0' and line[i] <= '9' and i < first_index:
            first_index = i
            val = int(line[i])

    return val

def find_last_number(line):

    val = 0
    last_index = -1
    for num in nums:
        if line.rfind(num) > last_index and line.rfind(num) != -1:
            val = nums.index(num)+1
            last_index = line.rfind(num)

    for i in range(len(line)-1, last_index, -1):
        if line[i] > '0' and line[i] <= '9' and i > last_index:
            val = int(line[i])
            last_index = i

    return val

def mysoln():
    f = open("p1input.txt", "r")
    lines = f.read().split("\n")

    total = 0
    first = None
    last = None
    i=1

    for line in lines:
        first = find_first_number(line)
        last = find_last_number(line)

        total += first*10+last

    print(total)

def theirsoln():
    f = open("p1input.txt", "r")
    lines =

    nums = re.findall("\d", line)
    total += int(nums[0] + nums[-1])

mysoln()
