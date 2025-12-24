from utils import read_file

from typing import Dict, Optional

class Server:
    mapping: Dict[str, list[str]]
    memory: dict[str, dict[str, int]]

    def __init__(self, lines: list[str]):
        self.mapping = {}
        self.memory = {}
        
        for line in lines:
            parts = line.split(":")
            key = parts[0]
            
            values = parts[1].split()
            self.mapping[key] = values

    def solve_helper(self, start, end) -> int:
        if start == end:
            return 1
        
        if start in self.memory and end in self.memory[start]:
            return self.memory[start][end]
        
        values = self.mapping.get(start, [])
        
        total = 0
        for state in values:
            total += self.solve_helper(state, end)
            
        if start not in self.memory:
            self.memory[start] = {}
        self.memory[start][end] = total
        
        return total

    def solve_1(self) -> int:
        start = "you"
        goal = "out"

        return self.solve_helper(start, goal)
    
    def solve_2(self) -> int:
        start = "svr"
        dac = "dac"
        fft = "fft"
        out = "out"

        # sdfo
        sd = self.solve_helper(start, dac)
        df = self.solve_helper(dac, fft)
        fo = self.solve_helper(fft, out)
        sdfo = sd * df * fo

        # sfdo
        sf = self.solve_helper(start, fft)
        fd = self.solve_helper(fft, dac)
        do = self.solve_helper(dac, out)
        sfdo = sf * fd * do
        
        return sdfo + sfdo

def solve_1(filename: str) -> int:    
    total: int = 0
    
    lines: list[str] = read_file(filename, "\n")

    server = Server(lines)
    
    total = server.solve_1()
    
    print(f"1. Total paths: {total}")
    
    return total

def solve_2(filename: str) -> int:    
    total: int = 0
    
    lines: list[str] = read_file(filename, "\n")

    server = Server(lines)
    
    total = server.solve_2()
    
    print(f"2. Total paths: {total}")
    
    return total

if __name__ == "__main__":
    solve_1("./input/day_11.csv")
    solve_2("./input/day_11.csv")