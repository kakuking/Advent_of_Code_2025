from utils import read_file
from typing import Tuple

from shapely.geometry import Polygon, box

class Corner:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        

def corner_area(first: Corner, second: Corner) -> int:
    return (abs(first.x - second.x) + 1) * (abs(first.y - second.y) + 1)

def max_rectangle_from_vertices(poly: Polygon):
    vertices = list(poly.exterior.coords)[:-1]  # remove duplicate last point

    best_area = 0
    best_rect = None
    best_corners = None

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        for j in range(i + 1, len(vertices)):
            x2, y2 = vertices[j]

            if x1 == x2 or y1 == y2:
                continue  # zero-area rectangle

            xmin, xmax = sorted([x1, x2])
            ymin, ymax = sorted([y1, y2])

            rect = box(xmin, ymin, xmax, ymax)
            corners = [Corner(xmin, ymin), Corner(xmax, ymax)]
            # covers() allows boundary-touching rectangles
            if poly.covers(rect):
                area = rect.area
                if area > best_area:
                    best_area = area
                    best_rect = rect
                    best_corners = corners

    return best_corners, best_area

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

def solve_2(filename: str) -> int:
    max_area: int = 0
    
    lines = read_file(filename, "\n")
    corners: list[Tuple[float, float]] = []
    for line in lines:
        nums = [int(num) for num in line.split(",")]
        corners.append((nums[0], nums[1]))
    
    poly = Polygon(corners)
    
    rect, _ =  max_rectangle_from_vertices(poly)
    area = corner_area(rect[0], rect[1])
    
    print(f"2. Largest area possible: {area}")
    return area

if __name__ == "__main__":
    solve_1("./input/day_9.csv")
    solve_2("./input/day_9.csv")