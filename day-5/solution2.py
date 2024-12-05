import sys
from functools import cmp_to_key

def main(filename):

    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
        rules = []
        printjobs = []
        for line in data:
            if "|" in line:
                rules.append(tuple([int(x) for x in line.split("|")]))
            elif "," in line:
                printjobs.append([int(x) for x in line.split(",")])

        part1and2(rules,printjobs)

def part1and2(rules, printjobs):

    def compare(l, r):
        # less than return -1
        # equal return 0
        # greater than return 1
        if (l, r) in rules:
            return -1
        if (r, l) in rules:
            return 1
        else:
            return 0

    tally = 0
    tally2 = 0

    for job in printjobs:
        sorted_job = sorted(job, key=cmp_to_key(compare))
        if job == sorted_job:
            tally += job[len(job)//2]
        else:
            tally2 += sorted_job[len(job)//2]

    print(tally)
    print(tally2)

        
if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
