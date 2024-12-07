import sys

class Node:
    def __init__(self, data):
        self.mul = None
        self.add = None
        # uncomment for part2
        self.concat = None
        self.data = data

    def build_tree(self, numbers, result):
        mul_res = None
        add_res = None
        # uncomment for part2
        concat_res = None
        if numbers:
            self.mul = Node(self.data * numbers[0])
            self.add = Node(self.data + numbers[0])
            # uncomment for part2
            self.concat = Node(int(str(self.data) + str(numbers[0])))
            # now 50% faster:
            if self.concat.data > result and self.mul.data > result and self.add.data > result:
                return None
            mul_res = self.mul.build_tree(numbers[1:], result)
            add_res = self.add.build_tree(numbers[1:], result)
            # uncomment for part2
            concat_res = self.concat.build_tree(numbers[1:], result)
            if mul_res:
                return mul_res
            if add_res:
                return add_res
            #uncomment for part2
            if concat_res:
                return concat_res
        else:
            if self.data == result:
                return self.data

def main(filename):
    with open(filename, "r") as file:
        data = [[[int(y) for y in x.split()] for x in line.strip().split(":")] for line in file]
        #print(data)
        part1or2(data)

def part1or2(data):
    tally = 0
    for equation in data:
        result = equation[0][0]
        numbers = equation[1]
        root = Node(numbers[0])
        r = root.build_tree(numbers[1:], result)
        if r:
            tally += r
    print(tally)

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
