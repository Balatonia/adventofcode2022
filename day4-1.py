with open('input.txt') as f:
    input = f.read().split("\n")

def get_elf_pairs(input):
    pair_list = []
    for i in input:
        pair = i.split(",")
        first_elf = pair[0].split("-")
        second_elf = pair[1].split("-")
        all_sections_first = list(range(int(first_elf[0]), int(first_elf[1])+1))
        all_sections_second = list(range(int(second_elf[0]), int(second_elf[1]) + 1))
        both_elves = [all_sections_first, all_sections_second]
        pair_list.append(both_elves)
    return pair_list

new_input = get_elf_pairs(input)
counter = 0
for i in new_input:
    if set(i[0]).issubset(i[1]) or set(i[1]).issubset(i[0]):
        counter += 1

print(counter)

## PART 2

total_counter = 0
for j in new_input:
    overlap = set(j[0]) & set(j[1])
    if overlap:
        total_counter += 1

print(total_counter)
