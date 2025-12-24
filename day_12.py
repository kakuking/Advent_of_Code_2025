from utils import read_file

from typing import Tuple

class Problem:
    grid: Tuple[int, int]
    counts: list[int]
    
    def __init__(self, line: str):
        parts = line.split(":")
        
        grid_str = parts[0].split("x")
        counts_str = parts[1].split()
        
        self.grid = (int(grid_str[0]), int(grid_str[1]))
        self.counts = [int(count) for count in counts_str]        

    def solve_1(self) -> bool:
        grid_area = self.grid[0] * self.grid[1]
        
        total_counts = sum(self.counts)
        
        return grid_area > total_counts * 8

def solve_1(filename) -> int:
    total: int = 0
    
    lines = read_file(filename, "\n\n")
    
    shapes: list[str] = []
    
    for line in lines[:-1]:
        parts = line.split(":")
        shape = parts[1][1:]

        shapes.append(shape)

    problem_lines = lines[-1].split("\n")
    
    for line in problem_lines:
        problem = Problem(line)
        if problem.solve_1():
            total += 1
    
    print(f"1. Total levels that are feasible: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_12.csv")