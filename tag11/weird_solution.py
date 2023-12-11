from functools import cache
from itertools import combinations

is_p2 = True

with open("input_emi.txt", "r") as file:
    grid = file.read().splitlines()

@cache
def is_empty_row(y):
    return not any((x == "#" for x in grid[y]))

@cache
def is_empty_col(x):
    return not any((line[x] == "#" for line in grid))

@cache
def expand_xy(x, y):
    scale = 1_000_000 if is_p2 else 2
    return (
        sum((scale if is_empty_col(ys) else 1 for ys in range(x))),
        sum((scale if is_empty_row(ys) else 1 for ys in range(y))),
    )

def dist(p1, p2):
    x3, y3 = expand_xy(*p1)
    x4, y4 = expand_xy(*p2)
    return abs(y4 - y3) + abs(x4 - x3)

def gal_coro():
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "#":
                yield x, y

print(
    "total sum distances:", 
    sum(dist(p1, p2) for p1, p2 in combinations(gal_coro(), 2))
)
