import sys, itertools

def main(filename):
    with open(filename, "r") as file:
        data = [[int(x) for x in line.strip().split()] for line in file]
        part1(data)
        part2(data)

def rule1(report):
    return all(0 < abs(i-j) <= 3 for i,j in zip(report[:-1], report[1:]))

def rule2(report):
    return report in (sorted(report), sorted(report, reverse=True))

def part1(data):
    safe_reports = sum((rule1(report) and rule2(report)) for report in data)
    print(safe_reports)

def tolerant_check(report):
    tolerant_reports = [list(x) for x in itertools.combinations(report, len(report) - 1)]
    return any([(rule1(report) and rule2(report)) for report in tolerant_reports])

def part2(data):
    safe_reports = sum([tolerant_check(report) for report in data])
    print(safe_reports)

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
