from map.paper_map import PaperMap

def fold_paper():
    marked_coords = []
    fold_list = []
    width = 0
    height = 0

    with open('day_thirteen/input.txt') as f:
        lines = f.read().splitlines()

        for line in lines:
            if len(line.strip()) < 1:
                continue
            
            if line.startswith('fold'):
                instructions, amount = line.split('=')
                axis = instructions.split(' ')[-1]

                fold_list.append({ axis: int(amount) })
                continue

            coords = [int(c) for c in line.split(',')]

            if width < coords[0]:
                width = coords[0]

            if height < coords[1]:
                height = coords[1]

            marked_coords.append(coords)

    width += 1
    height += 1
    paper_map = PaperMap(width, height)
    for coord in marked_coords:
        paper_map.mark_paper(coord)

    paper_map.fold_paper(fold_list[0])

    return paper_map.get_marked_count()

print(fold_paper())