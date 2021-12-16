from polymerization.polymer_template import PolymerTemplate

def grow_polymer():

    rules = {}
    base_string = ''

    with open('day_14/input.txt') as f:
        lines = f.read().splitlines()
        for idx, line in enumerate(lines, start=0):
            if len(line.strip()) < 1:
                continue

            if idx == 0:
                base_string = line
                continue
            
            pair, result = line.split(' -> ')
            rules[pair] = result

    polymer = PolymerTemplate(base_string=base_string, rules=rules)

    for _ in range(10):
        polymer.grow_polymer()
    
    highest = polymer.get_highest_count()
    lowest = polymer.get_lowest_count()

    return highest - lowest

print(grow_polymer())