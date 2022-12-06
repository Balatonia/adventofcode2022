import string

with open('input.txt') as f:
    input = f.read().split("\n")

def get_priority_of_shared_item(rucksack):
    half = len(rucksack) // 2
    first_half = rucksack[:half]
    second_half = rucksack[half:]
    shared_item = list(set(first_half) & set(second_half))[0]
    alphabet = list(string.ascii_letters)
    priority = alphabet.index(shared_item) + 1
    return priority

total_priority = 0
for i in input:
    total_priority += get_priority_of_shared_item(i)

## second part

def get_group_of_elves(elflist):
    n = 3
    all_groups = [elflist[i:i + n] for i in range(0, len(elflist), n)]
    return all_groups

def get_priority_of_badge(three_items):
    shared_item = list(set(three_items[0]) & set(three_items[1]) & set(three_items[2]))[0]
    alphabet = list(string.ascii_letters)
    priority = alphabet.index(shared_item) + 1
    return priority

total_badge = 0
groups_of_elves = get_group_of_elves(input)
for i in groups_of_elves:
    total_badge += get_priority_of_badge(i)

print(total_badge)

