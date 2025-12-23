from utils import read_file

class Corner:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def corner_area(first: Corner, second: Corner) -> int:
    return abs(first.x - second.x + 1) * abs(first.y - second.y + 1)

def solve_1(filename: str) -> int:
    max_area: int = 0
    
    lines = read_file(filename, "\n")
    corners: list[Corner] = []
    
    for line in lines:
        nums = [int(num) for num in line.split(",")]
        corners.append(Corner(nums[0], nums[1]))
    
    for i, corner in enumerate(corners):
        for other in corners[i+1:]:
            area = corner_area(corner, other)
            max_area = max(area, max_area)
    
    print(f"1. Largest area possible: {max_area}")
    return max_area

if __name__ == "__main__":
    solve_1("./input/day_9.csv")