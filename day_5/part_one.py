from vent_manager.vent_grid import VentGrid

def get_overlapping_lines():
    line_segments = []

    with open('day_5/input.txt') as f:
        lines = f.read().splitlines()
        for s in lines:
            line_segment = []

            line_points = s.split(' -> ')
            line_segment.append([int(coord) for coord in line_points[0].split(',')])
            line_segment.append([int(coord) for coord in line_points[1].split(',')])

            line_segments.append(line_segment)

    vent_grid = VentGrid()

    for line in line_segments:
        vent_grid.mark_vent(line)

    return vent_grid.get_points_where_lines_overlap()

print(get_overlapping_lines())