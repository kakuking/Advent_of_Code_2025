from typing import Optional

from utils import read_file

def greedy_2_max_joltage(joltage: str) -> int:
    max_joltage: int = 0

    for i in range(len(joltage) - 1):
        for j in range(i + 1, len(joltage)):
            ij = int(joltage[i])
            jj = int(joltage[j])

            cur_joltage = 10 * ij + jj
            
            max_joltage = max(cur_joltage, max_joltage)
    
    return max_joltage

def greedy_n_max_joltage(joltage: str, n: int = 12) -> Optional[int]:
    
    if n > len(joltage):
        return None
    if n == 1:
        return max(int(j) for j in joltage)
    if n == 2:
        return greedy_2_max_joltage(joltage)

    total_joltage: int = 0
    
    max_joltage: int = 0
    max_idx: int = 0
    
    search_range = len(joltage) - n + 1
    
    for i in range(search_range):
        j = joltage[i]
        if int(j) > max_joltage:
            max_idx = i
            max_joltage = int(j)
    
    remaining_joltage = greedy_n_max_joltage(joltage[max_idx+1:], n-1)
    
    if remaining_joltage is None:
        return None

    total_joltage = max_joltage * (10**(n-1)) + remaining_joltage
    
    return total_joltage

def solve_1(filename: str) -> int:
    total: int = 0

    joltages = read_file(filename, "\n")
    
    for joltage in joltages:
        total += greedy_2_max_joltage(joltage)
        
    print(f"1. Total joltage: {total}")
    
    return total

def solve_2(filename: str, n=12) -> int:
    total_joltage: int = 0

    joltages = read_file(filename, "\n")
    
    for joltage in joltages:
        res = greedy_n_max_joltage(joltage, n=n)
        total_joltage += 0 if res is None else res
    
    print(f"2. Total joltage: {total_joltage}")
    
    return total_joltage

if __name__ == "__main__":
    solve_1("./input/day_3.csv")
    solve_2("./input/day_3.csv", n=2)
    solve_2("./input/day_3.csv")