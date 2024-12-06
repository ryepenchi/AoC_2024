import sys
from itertools import cycle

def main(filename):

    with open(filename, "r") as file:
        data = [[x for x in line.strip()] for line in file.readlines()]
    print(len(data)*len(data[0]))
    #part1(data)
    part2(data)

step = {"^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)}

def vector1d_add(veca, vecb):
    return tuple([a + b for a, b in zip(veca, vecb)])

def part1(data):
        
    obstacles = []
    for row, line in enumerate(data):
        for column, character in enumerate(line):
            if character == "#":
                obstacles.append((row, column))

    orientations = ["^", ">", "v", "<",]

    # locate guard
    joinedgrid = "".join([j for i in data for j in i])
    for orientation in orientations:
        if orientation in joinedgrid:
            guardorientation = orientation

    orientation_cycle = cycle(orientations)
    while guardorientation != next(orientation_cycle):
        continue

    guard_column = joinedgrid.index(guardorientation) % len(data[0])
    guard_row = joinedgrid.index(guardorientation) // len(data[0])
    guard_starting_pos = (guard_row, guard_column)
    #print(guard_starting_pos)
    #print(guardorientation)

    visited = set()
    guard_pos = guard_starting_pos
    while 0 <= guard_pos[0] <= len(data)-1 and 0 <= guard_pos[1] <= len(data[0])-1:
        visited.add(guard_pos)
        new_guard_pos = vector1d_add(guard_pos, step[guardorientation])
        if new_guard_pos in obstacles:
            guardorientation = next(orientation_cycle)
        else:
            guard_pos = new_guard_pos

    print(len(visited))

def part2(data):

    # dumb solution runs for 15min
        
    obstacles = []
    for row, line in enumerate(data):
        for column, character in enumerate(line):
            if character == "#":
                obstacles.append((row, column))

    orientations = ["^", ">", "v", "<",]

    # locate guard
    joinedgrid = "".join([j for i in data for j in i])
    for orientation in orientations:
        if orientation in joinedgrid:
            guard_starting_orientation = orientation


    guard_column = joinedgrid.index(guard_starting_orientation) % len(data[0])
    guard_row = joinedgrid.index(guard_starting_orientation) // len(data[0])
    guard_starting_pos = (guard_row, guard_column)
    #print(guard_starting_pos)
    #print(guard_starting_orientation)

    HEIGHT = len(data)
    WIDTH = len(data[0])

    def patrol(obstacles):
        # init orientation
        orientation_cycle = cycle(orientations)
        while guard_starting_orientation != next(orientation_cycle):
            continue

        visited = set()
        guard_pos = guard_starting_pos
        guardorientation = guard_starting_orientation
        while 0 <= guard_pos[0] <= HEIGHT-1 and 0 <= guard_pos[1] <= WIDTH-1:
            if (guard_pos, guardorientation) in visited:
                return True
            else:
                visited.add((guard_pos, guardorientation))
                new_guard_pos = vector1d_add(guard_pos, step[guardorientation])
                if new_guard_pos in obstacles:
                    guardorientation = next(orientation_cycle)
                else:
                    guard_pos = new_guard_pos
        return False
  
    loop_obstacles = []

    print("HEIGHT", HEIGHT)
    print("WIDTH", WIDTH)

    for r in range(HEIGHT):
        for c in range(WIDTH):
            new_obstacle = (r,c)
            if c in [1, 129]:
                print((r,c))
            if new_obstacle in obstacles or new_obstacle == guard_starting_pos:
                continue
            else:
                is_loop = patrol(obstacles + [new_obstacle])
                if is_loop:
                    loop_obstacles.append(new_obstacle)
    
    print(len(loop_obstacles))
    #print(loop_obstacles)

        
if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)