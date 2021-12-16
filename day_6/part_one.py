from fish.lantern_fish import LanternFish

DAY_COUNT = 80

def count_laternfish():
    lanternfish = []

    with open('day_six/input.txt') as f:
        lanternfish = [LanternFish(internal_timer=int(fish)) for fish in f.readline().split(',')]
    
    spawn_count = len(lanternfish)

    for _ in range(DAY_COUNT):
        for fish in lanternfish:
            fish.respond_to_day()

    for lantfish in lanternfish:
        spawn_count += lantfish.count_children()

    return spawn_count    

print(count_laternfish())