from utils import read_file

class Manifold:
    def __init__(self, manifold_map: list[str]):
        self.manifold_map = manifold_map
        self.beams: list[int] = [manifold_map[0].index("S")]
        self.cur_idx = 1
        
        self.len_level = len(manifold_map[0])
        
        self.memory: list[list[int]] = [[-1 for _ in self.manifold_map[0]] for _ in self.manifold_map]
        
    def step_down(self) -> int:
        new_beams: list[int] = []
        num_splits = 0
        
        for beam in self.beams:
            char = self.manifold_map[self.cur_idx][beam]
            if char == ".":
                new_beams = self.add_beam(new_beams, beam)
            else:
                new_beams = self.add_beam(new_beams, beam-1)    # left
                new_beams = self.add_beam(new_beams, beam+1)    # right
                num_splits += 1
        
        self.cur_idx += 1
        self.beams = new_beams
        
        return num_splits
                
    def add_beam(self, new_beams: list[int], new_idx: int) -> list[int]:
        if new_idx in new_beams:
            return new_beams
        
        if new_idx < 0 or new_idx >= self.len_level:
            return new_beams

        new_beams.append(new_idx)
        return new_beams
    
    def count_timelines(self, beam, cur_idx) -> int:
        if self.memory[cur_idx-1][beam] != -1:
            return self.memory[cur_idx-1][beam]
        
        if cur_idx == len(self.manifold_map):
            return 1
        
        if beam < 0 or beam >= self.len_level:
            return 0
        
        new_beams: list[int] = []
        char = self.manifold_map[cur_idx][beam]
        
        if char == ".":
            return self.count_timelines(beam, cur_idx + 1)
        
        left_beam_timelines = self.count_timelines(beam - 1, cur_idx+1)
        right_beam_timelines = self.count_timelines(beam + 1, cur_idx+1)
        total_timelines = left_beam_timelines + right_beam_timelines

        self.memory[cur_idx-1][beam] = total_timelines
        
        return total_timelines
    
def solve_1(filename: str) -> int:
    total: int = 0
    
    manifold_map = read_file(filename, "\n")
    final_step = len(manifold_map)
    
    manifold = Manifold(manifold_map)
    
    for _ in range(1, final_step):
        total += manifold.step_down()

    print(f"Total tachyon beams: {total}")
    return total

def solve_2(filename: str) -> int:
    total: int = 0
    
    manifold_map = read_file(filename, "\n")
    final_step = len(manifold_map)
    
    manifold = Manifold(manifold_map)
    
    first_beam = manifold_map[0].index("S")
    total = manifold.count_timelines(first_beam, 1)    

    print(f"Total tachyon timelines: {total}")
    return total

if __name__ == "__main__":
    solve_1("./input/day_7.csv")
    solve_2("./input/day_7.csv")