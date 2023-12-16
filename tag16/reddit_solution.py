adj = lambda x, y: ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
nxt = lambda m, d: {
    "." : [d],
    "/" : [[(d - 1) % 4], [(d + 1) % 4]][d % 2],
    "\\": [[(d - 1) % 4], [(d + 1) % 4]][not d % 2],
    "-" : [[d], [(d - 1) % 4, (d + 1) % 4]][d % 2],
    "|" : [[d], [(d - 1) % 4, (d + 1) % 4]][not d % 2],
}[m]

with open("input.txt", "r") as file:
    data = file.read().splitlines()
    p2, rv, rh = 0, range(lv := len(data)), range(lh := len(data[0]))
    grid = {(x, y) : data[y][x] for x in rh for y in rv}
    for y_range, x_range, init_direction in [(rv, [0], 0), (rv, [lh - 1], 2), ([0], rh, 1), ([lv - 1], rh, 3)]:
        for y in y_range:
            for x in x_range:   
                queue, seen, energized = {((x, y), init_direction)}, set(), set()
                while queue:
                    current, direction = state = queue.pop()
                    energized.add(current)
                    seen.add(state)
                    neighbours = adj(*current)
                    for direction in nxt(grid[current], direction):
                        if (neighbour := neighbours[direction]) in grid and (next_state := (neighbour, direction)) not in seen:
                            queue.add(next_state)
                if not x + y + init_direction:
                    p1 = len(energized)
                p2 = max([p2, len(energized)])         
    print(p1, p2)