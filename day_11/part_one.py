from map.octomap import Octomap

def flash_octomap():
    number_map = []
    
    with open('day_11/input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            number_map.append([int(num_str) for num_str in line])

    octomap = Octomap(number_map)

    for _ in range(100):
        octomap.handle_one_step()
    
    return octomap.get_flash_count()

print(flash_octomap())