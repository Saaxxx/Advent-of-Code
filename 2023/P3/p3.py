spec_chars = ["*", "-", "$", "=", "+", "&", "@", "#", "/", "%"]

def check_around(data, line, start, end):

    surrounded = 0
    start_buff = -1
    end_buff = 1
    top_buff = -1
    bottom_buff = 1

    if start == 0:
        start_buff = 0
    if end == len(data[0])-1:
        end_buff = 0

    if line == 0:
        top_buff == 0
    if line == len(data)-1:
        bottom_buff = 0

    for i in range(line+top_buff, line+bottom_buff+1):
        for j in range(start+start_buff, end+end_buff+1):
            if data[i][j] in spec_chars:
                surrounded = 1
                break

    return surrounded

def part_one():
    f = open("p3input.txt")
    data = f.read().strip()
    lines = data.split("\n")
    total = 0
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] != "." and lines[i][j] not in spec_chars:
                k = j
                while k < len(lines[i]):
                    if not (lines[i][k] >= '0' and lines[i][k] <= '9'):
                        if check_around(lines, i, j, k-1):
                            total += int(lines[i][j:k])
                            j = k
                        break

                    elif k == len(lines[i]) - 1:
                        if check_around(lines, i, j, k):
                            total += int(lines[i][j:k+1])
                            j = k

                    k += 1

            j += 1
        i += 1

    print(total)
    f.close()

def check_gear(lines, line, index):
    top_buff = -1
    bottom_buff = 1
    left_buff = -1
    right_buff = 1

    adj_vals = []

    if index == 0:
        left_buff = 0
    if index == len(lines[0])-1:
        right_buff == 0
    if line == 0:
        top_buff == 0
    if line == len(lines)-1:
        bottom_buff = 0

    i = line+top_buff
    while i < line+bottom_buff+1:
        j = index+left_buff
        while j < index+right_buff+1:
            if ord(lines[i][j]) in range(ord('0'), ord('9')+1):

                num = lines[i][j]
                k = j-1
                while k >= 0 and ord(lines[i][k]) in range(ord('0'), ord('9')+1):
                    num = lines[i][k]+num
                    k-=1

                k = j+1
                while k < len(lines[0]) and ord(lines[i][k]) in range(ord('0'), ord('9')+1):
                    num += lines[i][k]
                    k+=1

                adj_vals.append(num)
                j = k-1

            j+=1
        i+=1

    return int(adj_vals[0])*int(adj_vals[1]) if len(adj_vals) == 2 else 0


def part_two():
    f = open("p3input.txt")
    data = f.read().strip()
    lines = data.split("\n")
    total = 0

    i=0
    while i < len(lines):
        j=0
        while j < len(lines[i]):
            if lines[i][j] == '*':
                total += check_gear(lines, i, j)
            j+=1
        i+=1

    print(total)
    return



part_one()
part_two()
