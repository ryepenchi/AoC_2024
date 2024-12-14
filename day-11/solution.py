import sys

def main(filename):

    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(" ")]

    print(data)
    part1(data)
    part2(data)


def part1(data):
    stones = data
    for _ in range(25):
        nextstones = []
        for stone in stones:
            if stone == 0:
                nextstones.append(1)
            elif len(stonestring := str(stone)) % 2 == 0:
                l = len(stonestring) // 2
                nextstones.append(int(stonestring[:l]))
                nextstones.append(int(stonestring[l:]))
            else:
                nextstones.append(stone * 2024)
        stones = nextstones
    #print(stones)
    print(len(stones))


def part2(data):

    def nextstone(stone):
        if stone == 0:
            return [1]
        elif len(stonestring := str(stone)) % 2 == 0:
            l = len(stonestring) // 2
            return [int(stonestring[:l]), int(stonestring[l:])]
        else:
            return [stone * 2024]
        
    def stones_after_blinks(stone_and_blinks):
        stone = stone_and_blinks[0]
        blinks = stone_and_blinks[1]
        nextstones = nextstone(stone)
        if blinks == 1:
            return len(nextstones)
        return sum([stones_after_blinks((x, blinks - 1)) for x in nextstones])
            
    def memoize(f): 
        memo = dict() 
        def func(n): 
            if n not in memo: 
                memo[n] = f(n) 
            return memo[n] 
        return func 

    stones_after_blinks = memoize(stones_after_blinks)

    stones = data
    blinks = 75
    totalstonesum = sum([stones_after_blinks((s, blinks)) for s in stones])
    print(totalstonesum)

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
