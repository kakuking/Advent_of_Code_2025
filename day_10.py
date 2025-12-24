from utils import read_file
from collections import deque

from typing import Dict

import pulp


class Indicators:
    lights: str
    buttons: list[list[int]]
    joltages: list[int]
    
    def __init__(self, problem_str: str):
        probs = problem_str.split()

        lights = probs[0][1:-1]
        buttons = probs[1:-1]
        joltages: str = probs[-1][1:-1]

        self.lights = lights
        
        self.buttons = []
        for button in buttons:
            button = button[1:-1]
            wiring = [int(wire) for wire in button.split(",")]
            
            self.buttons.append(wiring)
        
        self.joltages  = []      
        for joltage in joltages.split(","):
            self.joltages.append(int(joltage))

    def solve_1(self) -> float:
        start = "." * len(self.lights)
        target = "".join(self.lights)

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            lights, dist = queue.popleft()

            if lights == target:
                return dist

            for button in self.buttons:
                cur = list(lights)
                for idx in button:
                    cur[idx] = "." if cur[idx] == "#" else "#"

                nxt = "".join(cur)

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, dist + 1))

        return float("inf")

    def solve_2(self):
        target = self.joltages

        n = len(target)
        m = len(self.buttons)

        # Create problem
        prob = pulp.LpProblem("Joltage", pulp.LpMinimize)

        # Variables: how many times each button is pressed
        x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(m)]

        # Objective: minimize total presses
        prob += pulp.lpSum(x)

        # Constraints: Ax = b
        for i in range(n):
            prob += pulp.lpSum(x[j] for j in range(m) if i in self.buttons[j]) == target[i]

        # Solve
        status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

        if status != pulp.LpStatusOptimal:
            return float("inf")

        return int(pulp.value(prob.objective))

def solve_1(filename: str) -> float:
    total: float = 0
    
    lines = read_file(filename, "\n")
    
    for line in lines:
        indicator = Indicators(line)
        min_count = indicator.solve_1()

        total += min_count
        
    
    print(f"1. Lowest flips possible: {total}")
    return total

def solve_2(filename: str) -> float:
    total: float = 0
    
    lines = read_file(filename, "\n")
    
    for i, line in enumerate(lines):
        indicator = Indicators(line)
        min_count = indicator.solve_2()

        total += min_count
        
        print(f"{i}: {min_count}")
        
    print(f"2. lowest flips possible: {total}")
    return total

if __name__ == "__main__":
    # solve_1("./input/day_10.csv")
    solve_2("./input/day_10.csv")