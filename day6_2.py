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

    def turn_guard(self, temp_dir) -> int:
        if temp_dir == self.width * -1:
            return 1
        elif temp_dir == 1:
            return self.width
        elif temp_dir == self.width:
            return -1
        elif temp_dir == -1:
            return self.width * -1

    def check_pos_obs(self, known_obs : list[int]) -> int:
        temp_pos = self.guard_pos
        temp_dir = self.turn_guard(self.guard_dir)
        while self.lab_map[temp_pos + temp_dir] != "#":
            temp_pos += temp_dir
            if temp_pos in self.boundary:
                return None
        if (
                temp_pos + temp_dir in known_obs
                and
                self.lab_map[self.guard_pos + self.guard_dir] != "#"
            ):
            temp_obs = self.guard_pos + self.guard_dir
            return temp_obs
        else:
            return None
        
    def move_guard(self) -> None:
        visited_obs : list[int] = []
        pos_obs : list[int] = []
        while self.guard_pos not in self.boundary:
            while self.lab_map[self.guard_pos + self.guard_dir] != "#":
                self.guard_pos += self.guard_dir
                if self.guard_pos in self.boundary:
                    break
                temp_obs = self.check_pos_obs(visited_obs)
                if temp_obs:
                    pos_obs.append(temp_obs)
            if self.guard_pos + self.guard_dir not in visited_obs:
                visited_obs.append(self.guard_pos + self.guard_dir)
            self.guard_dir = self.turn_guard(self.guard_dir)
        print(len(pos_obs)) # (still) too low

def run(file_name):
    my_map = LabMap(file_name)
    my_map.move_guard()

if __name__ == "__main__":
    run("input6.txt")