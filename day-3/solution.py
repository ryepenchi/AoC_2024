import sys, re

def main(filename):
    with open(filename, "r") as file:
        data = file.read().strip()
        #print(data)
        part1(data)
        part2(data)

def part1(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = re.findall(pattern, data)
    mul_sum = sum(int(x)*int(y) for x,y in result)
    print(mul_sum)

def part2(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"
    result = re.findall(pattern, data)
    to_remove = []
    remove_toggle = False
    for i, item in enumerate(result):
        if remove_toggle or item[2] == "don't()":
            remove_toggle = True
            to_remove.append(i)
        if item[3] == "do()":
            remove_toggle = False
            to_remove.append(i)
    result = [x for i, x in enumerate(result) if i not in to_remove]
    mul_sum = sum(int(x)*int(y) for x,y,_,_ in result)
    print(mul_sum)


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
