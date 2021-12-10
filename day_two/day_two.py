DIRECTION = 'direction'
AMOUNT = 'amount'
FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

def handle_diving_input():
    movement_inputs = []

    with open("day_two/input.txt") as f:
        lines = f.readlines()
        for movement in lines:
            mvmt = movement.replace('\n', '')
            parts = mvmt.split(' ')
            movement_inputs.append({
                'direction': parts[0],
                'amount': int(parts[1])
            })

    horizonatal_pos = 0
    depth = 0

    for move in movement_inputs:
        direction = move[DIRECTION]
        amount = move[AMOUNT]

        if direction == FORWARD:
            horizonatal_pos += amount
            
        elif direction == DOWN:
            depth += amount

        elif direction == UP:
            depth -= amount

    return horizonatal_pos * depth

output = handle_diving_input()
print(output)