import sys

def main(filename):
    with open(filename, "r") as file:
        data = [[int(x) for x in line.strip().split()] for line in file]
        list1 = [row[0] for row in data]
        list2 = [row[1] for row in data]
        part1(list1, list2)
        part2(list1, list2)

def part1(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    distance_sum = sum(map(lambda x: abs(x[0]-x[1]), zip(list1, list2)))
    print(distance_sum)

def part2(list1, list2):
    similarity_score = sum((number * list1.count(number) * list2.count(number) for number in set(list1)))
    print(similarity_score)

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
