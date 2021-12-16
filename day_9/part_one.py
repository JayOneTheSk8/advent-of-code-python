from map.height_mapper import HeightMapper

def get_risk_assertion():

    number_map = []

    with open('day_nine/input.txt') as f:
        number_map += f.read().splitlines()
    
    height_mapper = HeightMapper(number_map=number_map)

    return height_mapper.get_risk_level()

print(get_risk_assertion())