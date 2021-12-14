from map.octomap import Octomap

def flash_octomap():
    number_map = []
    
    with open('day_eleven/input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            number_map.append([int(num_str) for num_str in line])

    octomap = Octomap(number_map)

    all_flashing = False
    step = 0

    while not all_flashing:
        octomap.handle_one_step()
        all_flashing = octomap.are_all_flashing()
        step += 1
    
    return step

print(flash_octomap())