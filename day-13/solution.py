import sys, re
import numpy as np


class Clawmachine:
    instances = []

    def __init__(self, regexresult):
        self.buttonAx = int(regexresult[0])
        self.buttonAy = int(regexresult[1])
        self.buttonBx = int(regexresult[2])
        self.buttonBy = int(regexresult[3])
        self.prizeX = int(regexresult[4])
        self.prizeY = int(regexresult[5])
        Clawmachine.instances.append(self)

    def __repr__(self):
        class_name = type(self).__name__
        return f"\n{class_name}\nButton A: X+{self.buttonAx}, Y+{self.buttonAy}\nButton B: X+{self.buttonBx}, Y+{self.buttonBy}\nPrize: X={self.prizeX}, Y={self.prizeY}"

    def solve(self):
        A = np.array([[self.buttonAx,self.buttonBx],[self.buttonAy,self.buttonBy]])
        B = np.array([self.prizeX,self.prizeY])
        return [x for x in np.linalg.solve(A,B)]
    
    def correct_prize_position(self, correction_value):
        self.prizeX += correction_value
        self.prizeY += correction_value

def main(filename):
    with open(filename, "r") as file:
        data = file.read()
        # print(data)
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)\n"
        results = re.findall(pattern, data)
        for result in results:
            Clawmachine(result)                
        #print(Clawmachine.instances)
        part1()
        part2()

def part1():
    tally = 0
    for clawmachine in Clawmachine.instances:
        A, B = clawmachine.solve()
        a, b = round(A), round(B)
        # print(clawmachine)
        # print(A, B)
        if abs(a - A) > 0.0000000001 or abs(b - B) > 0.0000000001:
            # print(f"no integer solution: {abs(a - A)} {abs(a - A) > 0.01}, {abs(b - B)} {abs(b - B) > 0.01}")
            continue
        if A > 100 or B > 100 or A < 0 or B < 0:
            # print("too many or negative presses")
            continue
            #print("more than 100 presses")
        else:
            # print(clawmachine)
            # print(A, B)
            # print("added!")
            # Button A: 3 tokens
            # Button B: 1 token
            tally += a * 3 + b
    print(tally) # 28262

def part2():
    tally = 0
    for clawmachine in Clawmachine.instances:
        clawmachine.correct_prize_position(10_000_000_000_000)
        A, B = clawmachine.solve()
        a, b = round(A), round(B)
        # print(clawmachine)
        # print(A, B)
        if abs(a - A) > 0.0001 or abs(b - B) > 0.0001:
            # print(f"no integer solution: {abs(a - A)}, {abs(b - B)}")
            continue
        if A < 0 or B < 0:
            # print("too many or negative presses")
            continue
            #print("more than 100 presses")
        else:
            # print(clawmachine)
            # print(A, B)
            # print("added!")
            tally += a * 3 + b
    print(tally)
    # 74564335127823 too low
    # 101406661266314


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
