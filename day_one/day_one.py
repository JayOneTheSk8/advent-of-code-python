def count_depth_measurement_increases():
    depth_measurement_increases = []
    increase_count = 0
    
    # Populate depth_measurement_increases
    with open("day_one/input.py") as f:
        lines = f.readlines()
        for measure in lines:
            m = int(measure.replace('\n', ''))
            depth_measurement_increases.append(m)

    prev_num = 0
    for idx, depth_measurement in enumerate(depth_measurement_increases, start=0):
        if idx == 0:
            prev_num = depth_measurement
            continue
        
        if depth_measurement > prev_num:
            increase_count += 1
        
        prev_num = depth_measurement
    
    return increase_count    

output = count_depth_measurement_increases()
print(output)