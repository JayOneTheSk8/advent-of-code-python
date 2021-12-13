def get_fuel_count(arr, pos):
    fuel_count = 0

    for num in arr:
        fuel_count += abs(num - pos)

    return fuel_count

def get_most_fuel_efficient_position(arr, lowest_num, highest_num):
    # Recursive B search
    if lowest_num > highest_num or lowest_num < 0 or highest_num < 0:
        return False

    rate_difference = int((highest_num - lowest_num) / 2)
    mid = lowest_num + rate_difference

    count_before = get_fuel_count(arr, mid - 1)
    count_current = get_fuel_count(arr, mid)
    count_after = get_fuel_count(arr, mid + 1)

    # Find position where forward and backward alignment are most expensive
    if count_before > count_current and count_current < count_after:
        return { 'best_pos': mid, 'fuel_count': count_current }
    
    # If lower numbers behind, look closer to lowest number
    if count_before < count_current and count_current < count_after:
        return get_most_fuel_efficient_position(arr, lowest_num, mid - 1)
    # If lower numbers ahead, look closer to highest number
    elif count_before > count_current and count_current > count_after:
        return get_most_fuel_efficient_position(arr, mid + 1, highest_num)

def get_fuel_input():
    positions = []

    with open('day_seven/input.txt') as f:
        positions += [int(p) for p in f.readline().split(',')]

    positions.sort()
    return positions

positions = get_fuel_input()
highest_num = positions[-1]
lowest_num = positions[0]

print(get_most_fuel_efficient_position(positions, lowest_num, highest_num))