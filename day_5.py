from utils import read_file

from typing import Tuple, Optional

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def contains(self, x):
        return x >= self.start and x <= self.end
    
def check_consolidate(first: Range, second: Range) -> Tuple[Range, Optional[Range]]:
    if first.end < second.start:
        return (first, second)
    
    if first.start > second.end:
        return (first, second)
    
    if first.contains(second.start) and first.contains(second.end):
        return (first, None)
    
    if second.contains(first.start) and second.contains(first.end):
        return (second, None)
    
    if first.contains(second.start):
        return (Range(first.start, second.end), None)
    
    if first.contains(second.end):
        return (Range(second.start, first.end), None)
    
    return (first, second)

def consolidate(ranges: list[Range]) -> list[Range]:
    consolidated_ranges: list[Range] = ranges
    
    flag: bool = False
    
    i = 0
    j = 1
    
    while i < len(consolidated_ranges)-1:
        j = i + 1
        while j < len(consolidated_ranges):
            
            first = consolidated_ranges[i]
            second = consolidated_ranges[j]
            
            new_first, check = check_consolidate(first, second)
            
            if check is None:
                flag = True
                consolidated_ranges[i] = new_first
                consolidated_ranges.pop(j)
                
                break

            j += 1
        
        if flag:
            flag = False
            continue
        
        i += 1
    
    return consolidated_ranges

def solve_1(filename: str) -> int:
    total: int = 0
    
    data  = read_file(filename, ",")
    ranges_str = data[0].split('\n')
    ingredients = data[1].split('\n')

    ranges: list[Range] = []
    
    for i, range in enumerate(ranges_str):
        nums = range.split("-")
        start = int(nums[0])
        end = int(nums[1])
        
        ranges.append(Range(start, end))
        
    for ingredient in ingredients:
        ingredient = int(ingredient)
        
        for range in ranges:
            if range.contains(ingredient):
                total += 1
                break
    
    print(f"1. Total unspoilt ingredients: {total}")
    return total

def solve_2(filename: str) -> int:
    total: int = 0
    
    data  = read_file(filename, ",")
    ranges_str = data[0].split('\n')

    ranges: list[Range] = []
    
    for i, a_range in enumerate(ranges_str):
        nums = a_range.split("-")
        start = int(nums[0])
        end = int(nums[1])
        
        ranges.append(Range(start, end))
        
    
    ranges = consolidate(ranges)
    
    for range in ranges:
        total += range.end - range.start + 1

    print(f"2. Total fresh ingredients: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_5.csv")
    solve_2("./input/day_5.csv")