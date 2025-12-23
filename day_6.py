from utils import read_file

from typing import Tuple, Optional

class CephMath:
    def __init__(self, lines: list[str]):
        self.lines: list[str] = lines
        self.cur_idx: int = 0
    
    def read(self) -> list[str]:
        nums: list[str] = []
        
        for i, row in enumerate(self.lines):
            char = row[self.cur_idx]
            if char not in "0123456789":
                continue
            
            nums.append(char)
            
        self.inc_idx()
            
        return nums
    
    def inc_idx(self):
        self.cur_idx += 1

def solve_1(filename: str) -> int:
    total: int = 0
    
    lines  = read_file(filename, "\n")
    data = [line.split() for line in lines]
    
    ops = data.pop()
    data = [[int(num) for num in row] for row in data]
    
    problems = len(ops)
    
    for problem in range(problems):
        ans = 0 if ops[problem] == "+" else 1
        
        for row in data:
            if ops[problem] == "+":
                ans += row[problem]
            else:
                ans *= row[problem]
        
        total += ans
    
    print(f"1. Total sum: {total}")
    return total

def solve_2(filename: str) -> int:
    total: int = 0
    
    lines  = read_file(filename, "\n")
    data = [line.split() for line in lines]
    
    # data = [[s[::-1] for s in row] for row in data]
    
    ops = data.pop()
    lines.pop()
    lines = [line + " " for line in lines]
    
    problems = len(ops)
    
    maths = CephMath(lines)
    cur_prob = 0
    nums: list[list[int]] = [[] for _ in ops]
    while cur_prob < problems:
        digits = maths.read()

        if len(digits) == 0:
            cur_prob += 1
            continue
        
        num = "".join(digits)
        nums[cur_prob].append(int(num))
        
        # print(f"problem {cur_prob}, num: {num}")
    
    for problem in range(problems):
        ans = 0 if ops[problem] == "+" else 1
        
        for num in nums[problem]:
            if ops[problem] == "+":
                ans += num
            else:
                ans *= num
        
        total += ans
        
    print(f"2. Total sum: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_6.csv")
    solve_2("./input/day_6.csv")