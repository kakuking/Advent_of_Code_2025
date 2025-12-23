from utils import read_file

def into_parts(word: str, num_parts: int = 2) -> list[str]:
    parts = []
    part_len = len(word) // num_parts
    
    cur_idx = 0
    while cur_idx < len(word):
        parts.append(word[cur_idx:cur_idx+part_len])
        cur_idx += part_len
    
    return parts

def sum_pattern(start: int, end: int, included: list[bool], num_parts:int = 2) -> tuple[int, list[bool]]:
    total = 0
    
    for id in range(start, end+1):
        id_str = str(id)
        if len(id_str) % num_parts != 0:
            continue
        
        flag: bool = True
        
        parts = into_parts(id_str, num_parts)
        for i in range(len(parts) - 1):
            if parts[i] != parts[i+1]:
                flag = False
        
        if flag and not included[id - start]:
            total += id
            included[id - start] = True
    
    return (total, included)

def solve_1(filename: str) -> int:
    ranges= read_file(filename, ",")
    
    total = 0
    
    for a_range in ranges:
        nums = a_range.split("-")
        start = int(nums[0])
        end = int(nums[1])
        
        num_included: list[bool] = [False for _ in range(start, end+1)]

        new_total, _= sum_pattern(start, end, num_included, 2)
        total += new_total
    
    print(f"Total of the fraudulent ids is: {total}")
    return total

def solve_2(filename: str) -> int:
    ranges= read_file(filename, ",")
    
    total = 0
    
    for a_range in ranges:
        nums = a_range.split("-")
        start = int(nums[0])
        end = int(nums[1])
        
        min_parts: int = 2
        max_parts: int = len(str(end))

        num_included: list[bool] = [False for _ in range(start, end+1)]
        
        for num_parts in range(min_parts, max_parts+1):
            new_total, num_included = sum_pattern(start, end, num_included, num_parts)

            total += new_total
    
    print(f"Total of the new fraudulent ids is: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_2.csv")
    solve_2("./input/day_2.csv")