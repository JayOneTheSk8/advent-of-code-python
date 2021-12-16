ZEROES = 'zeroes'
ONES = 'ones'

def convert_binary_string_to_decimal(binary_str):
    result = 0
    exponent = len(binary_str) - 1

    for char in binary_str:
        num = int(char)
        result += num * 2 ** exponent

        exponent -= 1

    return result

def analyze_binary_list(binary_list, position):
    counts = {
        ONES: 0,
        ZEROES: 0
    }

    for binary_str in binary_list:
        
        if binary_str[position] == '1':
            counts[ONES] += 1
        else:
            counts[ZEROES] += 1
    
    return counts

def get_life_support_rating():
    
    input_list = []

    with open("day_3/input.txt") as f:
        lines = f.readlines()

        for byte_str in lines:
            input_list.append(byte_str.replace('\n', ''))
    
    length_limit = len(input_list)

    # Calculate O2 rating
    oxygen_rating_list = list(input_list)
    oxygen_rating_binary = ''

    for pos in range(length_limit):
        if len(oxygen_rating_list) < 2:
            oxygen_rating_binary = oxygen_rating_list[0]
            break

        current_count = analyze_binary_list(oxygen_rating_list, pos)

        chosen_num = '1'
        if current_count[ZEROES] > current_count[ONES]:
            chosen_num = '0'
        
        oxygen_rating_list  = list(filter(lambda binary_str: binary_str[pos] == chosen_num, oxygen_rating_list))
    
    if len(oxygen_rating_binary) == 0:
        oxygen_rating_binary = oxygen_rating_list[0]

    # Calculate CO2 rating

    c_dioxide_rating_list = list(input_list)
    c_dioxide_rating_binary = ''

    for pos in range(length_limit):
        
        if len(c_dioxide_rating_list) < 2:
            c_dioxide_rating_binary = c_dioxide_rating_list[0]
            break

        current_count = analyze_binary_list(c_dioxide_rating_list, pos)

        chosen_num = '0'
        if current_count[ZEROES] > current_count[ONES]:
            chosen_num = '1'
        
        c_dioxide_rating_list = list(filter(lambda binary_str: binary_str[pos] == chosen_num, c_dioxide_rating_list))
    
    if len(c_dioxide_rating_binary) == 0:
        c_dioxide_rating_binary = c_dioxide_rating_list[0]
    
    oxygen_rating = convert_binary_string_to_decimal(oxygen_rating_binary)
    c_dioxide_rating = convert_binary_string_to_decimal(c_dioxide_rating_binary)

    return oxygen_rating * c_dioxide_rating

print(get_life_support_rating())