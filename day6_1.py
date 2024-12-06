'''
Rules:
- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.

Challenge:
How many distinct positions, including the guard's starting position, 
will the guard visit before leaving the mapped area?
'''

from aoc_common import read_file
import re

class LabMap():
    def __init__(self, file_name : str) -> None:
        self.load_map(file_name)
        self.guard_dir = self.width * -1
        self.set_boundary()

    def load_map(self, file_name : str) -> None:
        my_data = read_file(file_name)
        self.width : int = my_data.find("\n")
        self.lab_map : str = re.sub("\\n", "", my_data)
        self.height : int = len(self.lab_map) // self.width
        self.guard_pos : int = self.lab_map.find("^")

    def set_boundary(self) -> None:
        bottom_row = self.width * (self.height -1)
        # top boundary
        self.boundary : list[int] = [pos for pos in range(self.width)]
        # left boundary
        self.boundary += [pos * self.height for pos in range(1, self.width -1)]
        # right boundary
        self.boundary += [(pos * self.height) - 1 for pos in range(2, self.width)]
        # bottom boundary
        self.boundary += [pos + bottom_row for pos in range(self.width)]

    def turn_guard(self) -> None:
        if self.guard_dir == self.width * -1:
            self.guard_dir = 1
        elif self.guard_dir == 1:
            self.guard_dir = self.width
        elif self.guard_dir == self.width:
            self.guard_dir = -1
        elif self.guard_dir == -1:
            self.guard_dir = self.width * -1

    def move_guard(self) -> None:
        visited_pos = [self.guard_pos]
        while self.guard_pos not in self.boundary:
            while self.lab_map[self.guard_pos + self.guard_dir] != "#":
                self.guard_pos += self.guard_dir
                if self.guard_pos not in visited_pos:
                    visited_pos.append(self.guard_pos)
                if self.guard_pos in self.boundary:
                    break
            self.turn_guard()
        print(len(visited_pos))

def run(file_name):
    my_map = LabMap(file_name)
    my_map.move_guard()

if __name__ == "__main__":
    run("input6.txt")