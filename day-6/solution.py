import sys

def main(filename):

    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
        obstacles = []
        guard = tuple()
        guardstep = tuple()
        for row, line in enumerate(data):
            for column, character in enumerate(line):
                if character == "#":
                    obstacles.append((row, column))
                elif character in ("^", "v", "<", ">"):
                    guard = (row, column)
                    if character == "^":
                        guardstep = (-1, 0)
                    elif character == "v":
                        guardstep = (1, 0)
                    elif character == "<":
                        guardstep = (0, -1)
                    elif character == ">":
                        guardstep = (0, 1)

    print(obstacles)
    print(guard)
    print(guardstep)

    part1(data)
    part2(data)

def part1(data):
    
    def gridstep(data):
        pass

def part2(data):
    pass
        
if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)