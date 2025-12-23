from utils import read_file

def count_removable(floor_map: list[list[str]], rows: int, cols: int) -> tuple[int, list[list[bool]]]:
    total = 0
    
    removed: list[list[bool]] = [[False for _ in range(cols+2)] for _ in range(rows+2)]
    
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if floor_map[i][j] == ".":
                continue
            
            surround_count = 0
            
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    # print(f"{i+k}, {j+l} -> {k}, {l}")
                    
                    if floor_map[i+k][j+l] == "@":
                        surround_count += 1
            
            if surround_count < 4:
                total += 1
                removed[i][j] = True
    
    return (total, removed)

def solve_1(filename: str) -> int:    
    floor_map = read_file(filename, "\n")
    floor_map: list[list[str]] = [list(row) for row in floor_map]
    
    rows = len(floor_map)
    cols = len(floor_map[0])
    
    for i, row in enumerate(floor_map):
        floor_map[i] = ["."] + row + ["."]
        
    floor_map.insert(0, list("."*(cols+2)))
    floor_map.insert(rows, list("."*(cols+2)))
    
    total, _ = count_removable(floor_map, rows, cols)
    
    print(f"1. Total rolls that can be accessed: {total}")
    return total

def solve_2(filename: str) -> int:    
    total: int = 0
    floor_map = read_file(filename, "\n")
    floor_map: list[list[str]] = [list(row) for row in floor_map]
    
    rows = len(floor_map)
    cols = len(floor_map[0])
    
    for i, row in enumerate(floor_map):
        floor_map[i] = ["."] + row + ["."]
        
    floor_map.insert(0, list("."*(cols+2)))
    floor_map.insert(rows, list("."*(cols+2)))
    
    while True:
        cur_total, removed = count_removable(floor_map, rows, cols)
        
        if cur_total == 0:
            break
        
        total += cur_total
        
        for i, row in enumerate(removed):
            for j, col in enumerate(row):
                if col:
                    floor_map[i][j] = "."
    
    print(f"2. Total rolls that can be accessed: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_4.csv")
    solve_2("./input/day_4.csv")