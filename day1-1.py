with open('input.txt') as f:
    input = f.read().split("\n")

def create_list_of_elves(input_list):
    elf_list = [0]
    for i in input_list:
        if i:
            elf_list[-1] += int(i)
        else:
            elf_list.append(0)
    return elf_list

elves = create_list_of_elves(input)

print(max(elves))

## PART 2 ##

top_3_elves_together = sum(sorted(elves)[-3:])
print(top_3_elves_together)

