import numpy as np
import re
import sys
from copy import deepcopy

def solution(input):
    with open(input, 'r') as f:
        data_1, data_2 = f.read().split('\n\n')
    data_1, data_2 = data_1.split('\n')[:-1], [l for l in data_2.splitlines() if l]

    crates  = [[data_1[j][i] for i in range(1, len(data_1[-1]), 4)] for j in range(len(data_1))]
    crates = [list(x) for x in zip(*crates[::-1])]
    crates = list([c for c in crates[i] if c != ' '] for i in range(len(crates)))

    instructions = [re.findall(r"\d+", data_2[i]) for i in range(len(data_2))]
    instructions = [[int(j) for j in i] for i in instructions]

# Part 1 (list)
    crates_1 = deepcopy(crates)
    for i in range(len(instructions)):
        move = instructions[i][0]
        from_stack = instructions[i][1] - 1
        to_stack = instructions[i][2] - 1
        for j in range(move):
            crates_1[to_stack].append(crates_1[from_stack].pop(-1))
    sol_1 = ('').join([crates_1[i][-1] for i in range(len(crates_1))])


# Part 2 (np.array)
    for i in range(len(instructions)):
        move = instructions[i][0]
        from_stack = instructions[i][1] - 1
        to_stack = instructions[i][2] - 1
        crates[to_stack] = np.append(crates[to_stack], crates[from_stack][-move:])
        crates[from_stack] = crates[from_stack][:-move]
    sol_2 = ('').join([crates[i][-1] for i in range(len(crates))])

    return print(f"part_1 : {sol_1}\npart_2 : {sol_2}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = sys.argv[1] 
    else :
        input = 'input.txt'
    solution(input)