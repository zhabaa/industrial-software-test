from dataclasses import dataclass


@dataclass
class Gap:
    a: int
    b: int


with open("input_files/data_prog_contest_problem_1.txt", "r", encoding="utf-8") as file:
    n, *gaps = file.read().split("\n")
    gaps = sorted(
        [Gap(*map(int, gap.split("\t"))) for gap in gaps], 
        key=lambda gap: gap.b
    )

    points: list[int] = list()
    curr_point: int | None = None

    for gap in gaps:
        if curr_point is None or gap.a > curr_point:
            curr_point = gap.b
            points.append(curr_point)
    
    
    points_count = 0
    current_point = -float('inf')
    
    for gap in gaps:
        if gap.a > current_point:
            points_count += 1
            current_point = gap.b
            
    print(points_count)

    print(len(points))
