from typing import Tuple

Command = Tuple[str, int]

def separate_line(line: str) -> Command:
    dir = line[0]
    amount = int(line[1:])
    
    return (dir, amount)

def solve_1(filename: str) -> int:
    with open(filename, "r") as f:
        lines = f.readlines()
        
    commands: list[Command] = []

    for line in lines:
        commands.append(separate_line(line))

    cur_pos: int = 50
    num_zeros: int = 0

    for dir, amount in commands:
        step = amount if dir.upper() == "R" else -amount
        cur_pos += step
        cur_pos = cur_pos % 100

        if cur_pos == 0:
            num_zeros += 1

    print(f"Number of zeros encountered in {filename} : {num_zeros}")
    
    return num_zeros

def solve_2(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    commands: list[Command] = []

    for line in lines:
        commands.append(separate_line(line))

    prev_pos: int = 50
    cur_pos: int = 50
    num_zeros: int = 0

    for dir, amount in commands:
        step = 1 if dir.upper() == "R" else -1
        for _ in range(amount):
            cur_pos = (cur_pos + step) % 100
            if cur_pos == 0:
                num_zeros += 1

    print(f"Number of zeros passed in {filename} : {num_zeros}")

    return num_zeros

if __name__ == "__main__":
    solve_1("./input/day_1.csv")
    solve_2("./input/day_1.csv")