from utils import read_file

def into_parts(word: str, num_parts: int = 2) -> list[str]:
    parts = []
    part_len = len(word) // num_parts
    
    cur_idx = 0
    while cur_idx < len(word):
        parts.append(word[cur_idx:cur_idx+part_len])
        cur_idx += part_len
    
    return parts

def sum_pattern(start: int, end: int, num_parts:int = 2) -> int:
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
        
        if flag:
            # print(f"Fraudulent id: {id}")
            total += id
    
    return total

def solve_1(filename: str) -> int:
    ranges= read_file(filename, ",")
    
    total = 0
    
    for range in ranges:
        nums = range.split("-")
        start = int(nums[0])
        end = int(nums[1])
        
        total += sum_pattern(start, end, 2)
    
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
        
        for num_parts in range(min_parts, max_parts+1):
            total += sum_pattern(start, end, num_parts)
    
    print(f"Total of the new fraudulent ids is: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_2.csv")
    solve_2("./input/day_2.csv")