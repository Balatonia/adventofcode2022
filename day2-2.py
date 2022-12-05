with open('input.txt') as f:
    input = f.read().split("\n")

def get_result(input_str):
    opponent = input_str[0]
    result = input_str[-1]
    result_number = 0
    if result == "X":
        result_number += 0
        if opponent == "A":
            result_number += 3
        elif opponent == "B":
            result_number += 1
        elif opponent == "C":
            result_number += 2
    elif result == "Y":
        result_number += 3
        if opponent == "A":
            result_number += 1
        elif opponent == "B":
            result_number += 2
        elif opponent == "C":
            result_number += 3
    elif result == "Z":
        result_number += 6
        if opponent == "A":
            result_number += 2
        elif opponent == "B":
            result_number += 3
        elif opponent == "C":
            result_number += 1
    return result_number

total_score = 0
for i in input:
    total_score += get_result(i)

print(total_score)
