from nodes.cave_node import CaveNode, START, END

def find_all_paths():
    cave_nodes = {}

    with open('day_twelve/input.txt') as f:
        lines = f.read().splitlines()

        for connection in lines:
            caves = connection.split('-')
            first_cave_id = caves[0]
            second_cave_id = caves[1]

            first_node = CaveNode(first_cave_id) if first_cave_id not in cave_nodes else cave_nodes[first_cave_id]
            second_node = CaveNode(second_cave_id) if second_cave_id not in cave_nodes else cave_nodes[second_cave_id]

            if first_node.id == START:
                first_node.add_child(second_node)
            elif second_node.id == START:
                second_node.add_child(first_node)
            
            if first_node.id == END:
                second_node.add_child(first_node)
            elif second_node.id == END:
                first_node.add_child(second_node)
            
            if first_node.id not in [START, END] and second_node.id not in [START, END]:
                first_node.add_child(second_node)
                second_node.add_child(first_node)
            
            cave_nodes[first_node.id] = first_node
            cave_nodes[second_node.id] = second_node

    paths = cave_nodes[START].paths()

    return len(paths)

print(find_all_paths())