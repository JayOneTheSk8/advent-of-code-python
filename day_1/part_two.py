def check_bulk_measurement_increases():
    depth_measurement_increases = []
    increase_count = 0
    
    # Populate depth_measurement_increases
    with open("day_1/input.txt") as f:
        lines = f.readlines()
        for measure in lines:
            m = int(measure.replace('\n', ''))
            depth_measurement_increases.append(m)
    
    prev_sum = 0
    for idx, curr_depth_measurement in enumerate(depth_measurement_increases, start=0):
        next_measurement = None
        after_next_measurement = None
        try:
            next_measurement = depth_measurement_increases[idx + 1]
            after_next_measurement = depth_measurement_increases[idx + 2]
        except:
            pass

        if next_measurement and after_next_measurement:
            if idx == 0:
                prev_sum = curr_depth_measurement + next_measurement + after_next_measurement
                continue
            
            curr_sum = curr_depth_measurement + next_measurement + after_next_measurement
            if curr_sum > prev_sum:
                increase_count += 1
                
            prev_sum = curr_sum
    
    return increase_count

output = check_bulk_measurement_increases()
print(output)

        