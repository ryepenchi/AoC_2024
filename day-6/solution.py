import sys

def main(filename):

    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    print(data)

    part1(data)
    part2(data)

def part1(data):
    pass

def part2(data):
    pass
        
if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)