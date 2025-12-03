
f = open("p8input.txt", "r").read().strip()

directions = f.split("\n\n")[0]

code_parents = [x.split(" = ")[0] for x in f.split("\n\n")[1].split("\n")]
code_children = [x.split(" = ")[1].strip("()").split(", ") for x in f.split("\n\n")[1].split("\n")]

# code = "AAA"
#
# counter = 0
# while code != "ZZZ":
#     direction = directions[counter % len(directions)]
#
#     i = code_parents.index(code)
#     if direction == "R":
#         code = code_children[i][1]
#     else:
#         code = code_children[i][0]
#
#     counter += 1
#
# print(counter)

# part 2
def find_next_node(direction, code, code_parents, code_children):
    i = code_parents.index(code)
    return code_children[i][1] if direction == "R" else code_children[i][0]

start_codes = [x for x in code_parents if x[2] == "A"]
length_to_z = []

for i,code in enumerate(start_codes):
    counter = 0

    while code[2] != "Z":
        direction = directions[counter % len(directions)]
        code = find_next_node(direction, code, code_parents, code_children)
        counter += 1

    length_to_z.append(counter)
    length_to_z.append(start_codes[i])
    length_to_z.append(code)

print(length_to_z)


# def all_ending_with_z(codes):
#     for code in codes:
#         if code[2] != "Z":
#             return False
#     return True
#
#
# def part_2(start_codes, code_parents, code_children):
#     counter = 0
#     while not all_ending_with_z(start_codes):
#         direction = directions[counter % len(directions)]
#
#         for i,code in enumerate(start_codes):
#             start_codes[i] = find_next_node(direction, code, code_parents, code_children)
#
#         counter += 1
#         print(counter)
#     print(counter)
# part_2(start_codes, code_parents, code_children)
