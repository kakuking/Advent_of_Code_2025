from math import sqrt
from utils import read_file

from typing import Tuple

BoxId = int

class Box: 
    x: float
    y: float
    z: float

    circuit_id: int

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        self.circuit_id = -1
        
    def set_idx(self, idx: int):
        self.circuit_id = idx
    
    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

class Circuit:
    box_ids: list[BoxId]
    
    def __init__(self, boxes: list[BoxId]):
        self.box_ids = boxes
    
    def contains_box(self, box_id: BoxId) -> bool:
        return box_id in self.box_ids
    
    def add_box(self, box_id: BoxId):
        if box_id not in self.box_ids:
            self.box_ids.append(box_id)

def join_circuits(first: Circuit, second: Circuit) -> Circuit:
    for box_id in second.box_ids:
        first.add_box(box_id)
    
    return first
    
def distance(first: Box, second: Box) -> float:
    del_x = first.x - second.x
    del_y = first.y - second.y
    del_z = first.z - second.z
    
    return sqrt(del_x**2 + del_y**2 + del_z**2)

class BoxMap:
    def __init__(self, boxes: list[Box]):
        self.boxes = boxes
        self.num_boxes = len(boxes)
        self.circuits: list[Circuit] = []

        self.distances: list[list[float]] = [[float("inf")] * self.num_boxes for _ in range(self.num_boxes)]

        self.find_box_distances()
    
    def find_box_distances(self):
        for i, box in enumerate(self.boxes):
            for j in range(i+1, self.num_boxes):
                other_box = self.boxes[j]
                box_distance = distance(box, other_box)                
                self.distances[i][j] = box_distance
                self.distances[j][i] = box_distance
                
    def num_circuits(self) -> int:
        num = len(self.circuits)
        
        for box in self.boxes:
            if box.circuit_id == -1:
                num += 1
                
        return num
    
    def find_closest_pairs(self) -> list[tuple[int, int, float]]:
        valid_pairs = []
        
        for i, box in enumerate(self.boxes):
            for j in range(i+1, self.num_boxes):
                other_box = self.boxes[j]
                valid_pairs.append((self.distances[i][j], i, j))

        # Sort by distance and take top n
        valid_pairs.sort()
        
        return [(i, j, dist) for dist, i, j in valid_pairs]
    
    def join_closest_boxes(self, n: int=-1) -> float:
        min_distance = float("inf")
        closest_pairs = self.find_closest_pairs()
        last_join_prod = 0.0

        if n == -1:
            n = len(closest_pairs)
        
        for closest_pair in closest_pairs[:n]:
            i, j, _ = closest_pair
            box_1: Box = self.boxes[i]
            box_2: Box = self.boxes[j]
            
            last_join_prod = box_1.x * box_2.x
            
            circuit_1: int = box_1.circuit_id
            circuit_2: int = box_2.circuit_id
            
            # Both are not in a circuit
            if circuit_1 == -1 and circuit_2 == -1:
                circuit = Circuit([i, j])
                self.circuits.append(circuit) 
                self.boxes[i].circuit_id = len(self.circuits) - 1
                self.boxes[j].circuit_id = len(self.circuits) - 1
            # 1 is not in circuit, 2 is
            elif circuit_1 == -1:
                self.circuits[circuit_2].add_box(i)
                self.boxes[i].circuit_id = circuit_2
            # 2 is not in circuit, 1 is
            elif circuit_2 == -1:
                self.circuits[circuit_1].add_box(j)
                self.boxes[j].circuit_id = circuit_1
            # both are in circuits
            elif circuit_1 == circuit_2:
                continue
            else:
                self.circuits[circuit_1] = join_circuits(self.circuits[circuit_1], self.circuits[circuit_2])
                for id in self.circuits[circuit_2].box_ids:
                    self.boxes[id].circuit_id = circuit_1
                
                self.circuits.pop(circuit_2)
            
                # Update all boxes that pointed to circuits after circuit_2
                # (their indices shifted down by 1 after the pop)
                for box in self.boxes:
                    if box.circuit_id > circuit_2:
                        box.circuit_id -= 1
                        
            if self.num_circuits() == 1:
                break
        
        return last_join_prod

    def n_biggest_circuits(self, n: int = 3) -> list[int]:
        circuit_sizes = []
        
        for circuit in self.circuits:
            circuit_sizes.append(len(circuit.box_ids))
        
        for box in self.boxes:
            if box.circuit_id == -1:
                circuit_sizes.append(1)
        
        circuit_sizes.sort(reverse=True)
        
        return circuit_sizes[:n]

def solve_1(filename: str) -> int:
    total = 0

    lines = read_file(filename, "\n")
    boxes: list[Box] = []
    
    for line in lines:
        nums = [float(num) for num in line.split(",")]
        boxes.append(
            Box(nums[0], nums[1], nums[2])
        )
    
    boxmap = BoxMap(boxes)
    boxmap.join_closest_boxes(1000)
    
    biggest = boxmap.n_biggest_circuits(3)
    
    total = biggest[0] * biggest[1] * biggest[2]
    
    print(f"1. Total: {total}")
    
    return total

def solve_2(filename: str) -> int:
    total = 0

    lines = read_file(filename, "\n")
    boxes: list[Box] = []
    
    for line in lines:
        nums = [float(num) for num in line.split(",")]
        boxes.append(
            Box(nums[0], nums[1], nums[2])
        )
    
    boxmap = BoxMap(boxes)
    prod = boxmap.join_closest_boxes(-1)
    
    print(f"2. Total: {prod}")
    
    return total

if __name__ == "__main__":
    solve_1("./input/day_8.csv")
    solve_2("./input/day_8.csv")