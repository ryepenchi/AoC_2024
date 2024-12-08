import sys
import numpy as np


class Antenna:
    instances = []
    frequencies = set()

    def __init__(self, frequency, position):
        self.frequency = frequency
        self.position = np.array(position)
        Antenna.instances.append(self)
        Antenna.frequencies.add(self.frequency)
        self.antinodes = set()
        self.oob_an = set()
        self.harmonic_antinodes = set()
        self.oob_han = set()

    # part 1 debug repr
    # def __repr__(self):
    #     class_name = type(self).__name__
    #     return f"{class_name}(freq={self.frequency}, pos={self.position}, antinodes={self.antinodes}, oob_an={self.oob_an})"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(freq={self.frequency}, pos={self.position}, hantinodes={self.harmonic_antinodes}, oob_han={self.oob_han})"

    # gets only called on class
    def get_kind(frequency):
        return [
            antenna for antenna in Antenna.instances if antenna.frequency == frequency
        ]

    # gets only called on class
    def get_unique_antinodes():
        unique_antinodes = set()
        for antenna in Antenna.instances:
            unique_antinodes.update(antenna.antinodes)
        return unique_antinodes

    # gets only called on class
    def get_unique_harmonic_antinodes():
        unique_harmonic_antinodes = set()
        for antenna in Antenna.instances:
            unique_harmonic_antinodes.update(antenna.harmonic_antinodes)
        return unique_harmonic_antinodes

    # gets called on instances
    def get_own_kind(self):
        return [
            antenna
            for antenna in Antenna.instances
            if antenna.frequency == self.frequency
        ]

    def calc_antinodes(self, HEIGHT, WIDTH):
        for antenna in self.get_own_kind():
            if antenna == self:
                continue
            antinode = self.position - (antenna.position - self.position)
            lower_bounds = any(antinode < np.array((0, 0)))
            upper_bounds = any(antinode >= np.array((HEIGHT, WIDTH)))
            if lower_bounds or upper_bounds:
                self.oob_an.add(tuple(antinode))
                continue
            self.antinodes.add(tuple(antinode))

    def calc_harmonic_antinodes(self, HEIGHT, WIDTH):
        for antenna in self.get_own_kind():
            if antenna == self:
                continue
            vector = antenna.position - self.position
            lower_bounds, upper_bounds = False, False
            start_pos = self.position
            while (lower_bounds or upper_bounds) == False:
                antinode = start_pos + vector
                lower_bounds = any(antinode < np.array((0, 0)))
                upper_bounds = any(antinode >= np.array((HEIGHT, WIDTH)))
                if lower_bounds or upper_bounds:
                    self.oob_han.add(tuple(antinode))
                else:
                    self.harmonic_antinodes.add(tuple(antinode))
                    start_pos = antinode


def main(filename):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
        # print(data)
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if col != ".":
                    Antenna(col, (i, j))
        # for l in data:
        #     print(l)
        # print(f"Gridsize: {len(data)} x {len(data[0])}")
        part1(data)
        part2(data)


def part1(data):
    for antenna in Antenna.instances:
        # print(f"Calculating antinodes for ", antenna)
        antenna.calc_antinodes(len(data), len(data[0]))
    print(len(Antenna.get_unique_antinodes()))


def part2(data):
    for antenna in Antenna.instances:
        # print(f"Calculating antinodes for ", antenna)
        antenna.calc_harmonic_antinodes(len(data), len(data[0]))
    # for f in Antenna.frequencies:
    #     print(f"{f} Antennas: ")
    #     for a in Antenna.get_kind(f):
    #         print(a)
    print(len(Antenna.get_unique_harmonic_antinodes()))


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = "testinput.txt"
    main(filename)
