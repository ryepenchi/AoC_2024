import sys, re

def main(filename):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
        #print(data)
        part1(data)
        part2(data)

def part1(data):
    pattern = r"XMAS"

    # Transpose
    data_transposed = []
    for i in range(len(data[0])):
        data_transposed.append("".join([x[i] for x in data]))

    # Diagonals
    max_col = len(data[0])
    max_row = len(data)
    fdiag = ["" for _ in range(max_row + max_col - 1)]
    bdiag = ["" for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y] += data[y][x]
            bdiag[x-y-min_bdiag] += data[y][x]

    variants = [data, data_transposed, fdiag, bdiag]
    tally = 0

    for variant in variants:
        for line in variant:
            result = re.findall(pattern, line)
            tally += sum([bool(x) for x in result])
            # reversed
            result = re.findall(pattern, line[::-1])
            tally += sum([bool(x) for x in result])

    print(tally)

def part2(data):

    def check_xmas(data,x,y):
        # first diagonal
        d11 = data[y-1][x-1] == "M" and data[y+1][x+1] == "S"
        d12 = data[y-1][x-1] == "S" and data[y+1][x+1] == "M"
        d21 = data[y+1][x-1] == "M" and data[y-1][x+1] == "S"
        d22 = data[y+1][x-1] == "S" and data[y-1][x+1] == "M"
        return (d11 or d12) and (d21 or d22)

    tally = 0
    max_col = len(data[0])
    max_row = len(data)
    for x in range(1, max_col - 1):
        for y in range(1, max_row -1):
            if data[y][x] == "A":
                tally += check_xmas(data,x,y)
    print(tally)


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
