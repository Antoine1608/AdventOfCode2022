from itertools import product
import sys

def parse(entry) :
    with open(entry) as f:
        input = f.read().split("\n")[:-1]
    return [list(map(lambda x: int(x), input[i])) for i in range(len(input))]

# Part 1
def part1(entry) :
    input = parse(entry)
    count = 0
    for i, j in product(range(len(input)), range(len(input[0]))):
        if all([input[i][j] > x for x in input[i][j + 1 :]]):
            count += 1
        elif all([input[i][j] > x for x in input[i][:j]]):
            count += 1
        elif all([input[i][j] > x for x in [r[j] for r in input[i + 1 :]]]):
            count += 1
        elif all([input[i][j] > x for x in [r[j] for r in input[:i]]]):
            count += 1

    return print("part 1 : ", count)

# part 2
# Rm : 3 1 2 1 => le 3 voit 3 arbres et non 2 !
def view(grid: list, caban: tuple, dire: str) -> int:
    i, j = caban
    H = grid[i][j]
    n = 0

    if dire == "right":
        liste = grid[i][j + 1 :]
    if dire == "left":
        liste = grid[i][:j][::-1]
    if dire == "up":
        liste = [r[j] for r in grid[:i]][::-1]
    if dire == "down":
        liste = [r[j] for r in grid[i + 1 :]]

    for tree in liste:
        n += 1
        if tree >= H:
            break

    return n

def part2(entry):
    input = parse(entry)
    score = 0
    for i, j in product(range(len(input)), range(len(input[0]))):
        score_tree = (
            view(input, (i, j), "up")
            * view(input, (i, j), "down")
            * view(input, (i, j), "right")
            * view(input, (i, j), "left")
        )
        if score_tree > score:
            score = score_tree
            place = (i, j)

    return print("part 2 : ", score)

if __name__ == "__main__":
    input = sys.argv[1]
    part1(input)
    part2(input)